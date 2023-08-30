from django.shortcuts import render, redirect
from .forms import UserForm, AuthForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            #auth_login(request, user)
            return redirect('accounts:login')

    else:
        form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        form = AuthForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
        
    else:
        form = AuthForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def profile(request, username):
    pass