from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import UserTypeForm

def home(request):
    form = UserTypeForm()
    return render(request, 'home.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')
