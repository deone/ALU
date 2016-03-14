from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from django.conf import settings

from .forms import *
from .models import *
from .helpers import *

def home(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserTypeForm(user=request.user)

    announcements = Announcement.objects.all()
    doc_requests = DocumentRequest.objects.all()

    return render(request, 'home.html', {
      'form': form,
      'announcements': announcements,
      'document_requests': doc_requests,
      })

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
            announcement = form.save()
            email_students(announcement)
            messages.success(request, 'Announcement posted successfully.')
            return redirect('app:post_announcement')
    else:
        form = AnnouncementForm()

    return render(request, 'app/post_announcement.html', {'form': form})

# @login_required
class AnnouncementDetail(DetailView):
    model = Announcement
    context_object_name = 'object_detail'

@login_required
def document_request_detail(request, pk, slug):
    document_request = get_object_or_404(DocumentRequest, pk=pk)

    if request.method == 'POST':
        form = DocumentRequest(request.POST, request.FILES)
    else:
        form = DocumentForm()

    return render(request, 'app/documentrequest_detail.html', {'object_detail': document_request, 'form': form})

@login_required
def post_document_request(request):
    if request.method == 'POST':
        form = DocumentRequestForm(request.POST)
        if form.is_valid():
            doc_request = form.save()
            email_students(doc_request)
            messages.success(request, 'Document request posted successfully.')
            return redirect('app:post_document_request')
    else:
        form = DocumentRequestForm()

    return render(request, 'app/post_document_request.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect(settings.LOGIN_URL)
