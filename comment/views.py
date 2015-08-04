from django.shortcuts import render
from django.utils.html import escape
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import Comment

# Create your views here.
@login_required
def save(request, imdbID):
    text = escape(request.POST['comment'])
    user = escape(request.POST['user'])
    comment = Comment(imdb=imdbID, user=user, text=text, date=timezone.now())
    comment.save()
    # assume always successful for now
    return HttpResponseRedirect(reverse('movie:detail', args=(imdbID,)))
