from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.html import escape
from django.contrib.auth.views import logout_then_login

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = escape(request.POST['username'])
        password = escape(request.POST['password'])
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = {'error': 'Login Failed'}
            return render(request, 'login/index.html', error_message)
    else:
        return render(request, 'login/index.html', {})

def logout(request):
    return logout_then_login(request)
