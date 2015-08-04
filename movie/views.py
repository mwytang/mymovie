from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404
from django.utils.html import escape
from comment.models import Comment
from django.http import Http404
import urllib.request
import json

# Create your views here.
@login_required
def index(request):
    return render(request, 'movie/index.html', {})

@login_required
def search(request):
    value = escape(request.POST['value'])
    url = "http://www.omdbapi.com/?s=" + value + "&r=json"
    ret = urllib.request.urlopen(url)
    result = json.loads(ret.readall().decode('utf-8'))
    return render(request, 'movie/index.html', {
        'result': result,
    })

@login_required
def detail(request, imdbID):
    id = escape(imdbID)
    url =  "http://www.omdbapi.com/?i=" + id + "&r=json"
    ret = urllib.request.urlopen(url)
    result = json.loads(ret.readall().decode('utf-8'))
    try:
        comments = get_list_or_404(Comment.objects.order_by('-date'), imdb=id)
    except Http404:
        comments = []
    return render(request, 'movie/detail.html', {
        'detail': result,
        'comments': comments,
    })
