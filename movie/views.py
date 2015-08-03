from django.shortcuts import render

# Create your views here.
def index(request):
    example = 'Example'
    context = {'example': example}
    return render(request, 'movie/index.html', context)
