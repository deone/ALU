from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import *

import unicodecsv

def home(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserTypeForm(user=request.user)

    return render(request, 'home.html', {'form': form})

def import_list(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ImportForm()

    return render(request, 'app/import_list.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')
