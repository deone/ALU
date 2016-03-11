from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from app.models import Announcement, DocumentRequest

def make_context(obj, obj_type):
    current_site = Site.objects.get_current()

    return {
        'domain': current_site.domain,
        'obj': obj,
        'type': obj_type,
        'site_name': current_site.name,
        'protocol': 'http',
    }

def email_students(obj):
    if isinstance(obj, Announcement):
        subject = 'New Announcement: %s'
        obj_type = 'announcement'
    elif isinstance(obj, DocumentRequest):
        subject = 'New Document Request: %s'
        obj_type = 'document request'

    subject = subject % obj.title

    context = make_context(obj, obj_type)
    email_template = 'app/email.html'
    body = loader.render_to_string(email_template, context)
    to = [user.email for user in User.objects.filter(usertype__user_type='STD')]

    email_message = EmailMultiAlternatives(subject, body, 'no-reply@alu.com', to)
    email_message.attach_alternative(body, 'text/html')

    email_message.send()
