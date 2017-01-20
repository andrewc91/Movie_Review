from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('movies:index'))
    else:
        return render(request, 'login_app/index.html')

def registration(request):
    return render(request, 'login_app/register.html')

def create(request):
    if request.method == 'POST':
        result = User.objects.register(request.POST)

        if result[0] == True:
            request.session['user_id'] = result[1].id
            return redirect(reverse('movies:index'))
        else:
            for error in result[1]:
                messages.error(request, error, extra_tags="register")
            return redirect(reverse('users:registration'))

def login(request):
    if request.method == 'POST':
        result = User.objects.login(request.POST)

        if result[0] == True:
            request.session['user_id'] = result[1].id
            return redirect(reverse('movies:index'))
        else:
            for error in result[1]:
                messages.error(request, error, extra_tags="login")
            return redirect(reverse('users:index'))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect(reverse('users:index'))
