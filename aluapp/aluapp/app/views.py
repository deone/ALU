from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *

def home(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserTypeForm(user=request.user)

    return render(request, 'home.html', {'form': form})

@login_required
def import_list(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Students imported successfully.')
    else:
        form = ImportForm()

    return render(request, 'app/import_list.html', {'form': form})

@login_required
def post_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Announcement posted successfully.')
    else:
        form = AnnouncementForm()

    return render(request, 'app/post_announcement.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')
