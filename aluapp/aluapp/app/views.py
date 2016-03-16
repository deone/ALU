from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse

from utils.decorators import *
from utils import zipdir, create_email, send_email
from .forms import *
from .models import *

import datetime
import os

def home(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserTypeForm(user=request.user)

    announcements = Announcement.objects.all()
    document_requests = DocumentRequest.objects.all()
    document_types = DocumentType.objects.all()

    doc_type_list = []
    now = timezone.now()

    for doc_type in document_types:
        dct = {}
        dct['id'] = doc_type.pk
        dct['name'] = doc_type.document_type
        dct['today_count'] = doc_type.document_set.filter(
            date_submitted__gt=datetime.date(now.year, now.month, now.day - 1), date_submitted__lt=datetime.date(now.year, now.month, now.day + 1)
            ).count()
        dct['year'] = now.year
        dct['month'] = now.month
        dct['day'] = now.day
        dct['total_count'] = doc_type.document_set.count()
        doc_type_list.append(dct)

    return render(request, 'home.html', {
      'form': form,
      'announcements': announcements,
      'document_requests': document_requests,
      'document_types': doc_type_list,
      })

@login_required
@must_be_staff
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
@must_be_staff
def post_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save()

            params = create_email(obj=announcement)
            send_email(params['subject'], params['body'], params['to'])

            messages.success(request, 'Announcement posted successfully.')
            return redirect('app:post_announcement')
    else:
        form = AnnouncementForm()

    return render(request, 'app/post_announcement.html', {'form': form})

decorators = [login_required, must_be_student]

@method_decorator(decorators, name='dispatch')
class AnnouncementDetail(DetailView):
    model = Announcement
    context_object_name = 'object_detail'

@login_required
@must_be_student
def document_request_detail(request, pk, slug):
    document_request = get_object_or_404(DocumentRequest, pk=pk)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            doc_name = document.document.name
            document.user = request.user
            document.document_request = document_request
            document.document_type = document_request.document_type
            document.save()
            messages.success(request, 'Document uploaded successfully.')
            return redirect('home')
    else:
        form = DocumentForm()

    return render(request, 'app/documentrequest_detail.html', {'object_detail': document_request, 'form': form})

@login_required
@must_be_staff
def post_document_request(request):
    if request.method == 'POST':
        form = DocumentRequestForm(request.POST)
        if form.is_valid():
            doc_request = form.save()

            params = create_email(obj=doc_request)
            send_email(params['subject'], params['body'], params['to'])

            messages.success(request, 'Document request posted successfully.')
            return redirect('app:post_document_request')
    else:
        form = DocumentRequestForm()

    return render(request, 'app/post_document_request.html', {'form': form})

@login_required
def download_today_doc_type(request, doc_type_id, year, month, day):
    print doc_type_id, year, month, day

@login_required
def download_all_doc_type(request, doc_type_id):
    print doc_type_id

@login_required
def download_doc_type_by_date_range(request):
    pass

@login_required
@must_be_staff
def download_all(request):
    _file = zipdir(settings.MEDIA_ROOT, 'documents')

    zip_file = open(_file.filename, 'r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % _file.filename

    os.remove(_file.filename)

    return response

def mail_staff(request):
    print 'yes!'
    return HttpResponse

def logout(request):
    auth_logout(request)
    return redirect(settings.LOGIN_URL)
