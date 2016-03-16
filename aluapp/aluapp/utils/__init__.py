# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# from slugify import slugify as unicode_slugify

from django.db.models.fields import SlugField
from django.utils.encoding import smart_text
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.models import Site
from django.template import loader
from django.utils import timezone

import os
import zipfile
import datetime

__all__ = ['AutoSlugField', ]


class AutoSlugField(SlugField):
    """
    Auto populates itself from another field.

    It behaves like a regular SlugField.
    When populate_from is provided it'll populate itself on creation,
    only if a slug was not provided.
    """

    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop('populate_from', None)
        super(AutoSlugField, self).__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        default = super(AutoSlugField, self).pre_save(instance, add)

        if default or not add or not self.populate_from:
            return default

        inst = instance

        for attr in self.populate_from.split('.'):
            value = getattr(inst, attr)
            inst = value

        if value is None:
            return default

        # TODO: Django 1.9 will support unicode slugs
        # if settings.ST_UNICODE_SLUGS:
            # TODO: mark as safe?
            # slug = unicode_slugify(smart_text(value), ok='-')
            # pass
        # else:
        slug = slugify(smart_text(value))

        slug = slug[:self.max_length].strip('-')

        # Update the model’s attribute
        setattr(instance, self.attname, slug)

        return slug

    def deconstruct(self):
        name, path, args, kwargs = super(AutoSlugField, self).deconstruct()

        if self.populate_from is not None:
            kwargs['populate_from'] = self.populate_from

        return name, path, args, kwargs

def get_list(klass):
    lst = [('', 'Select')]

    for obj in klass.objects.all():
        if hasattr(obj, 'title'):
            tup = (obj.id, obj.title)
        else:
            tup = (obj.id, obj.document_type)
        lst.append(tup)

    return lst

def zipdir(src, dst):
    zf = zipfile.ZipFile('%s.zip' % dst, 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
            zf.write(absname, arcname)

    zf.close()
    return zf

def build_doc_type_lst(lst):
    now = timezone.now()

    doc_type_list = []
    for doc_type in lst:
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

    return doc_type_list

def make_context(obj=None, lst=None):
    current_site = Site.objects.get_current()
    context = {'site_name': current_site.name}

    if obj is not None:
        context.update({
            'domain': current_site.domain,
            'obj': obj,
            'type': obj.object_type,
            'protocol': 'http',
        })
    else:
        context.update({'document_types': build_doc_type_lst(lst)})

    return context

def create_email(user_type, obj=None, lst=None):
    if obj is not None:
        if obj.object_type == 'announcement':
            subject = 'New Announcement: %s' % obj.title
        if obj.object_type == 'document request':
            subject = 'New Document Request: %s' % obj.title
        email_template = 'app/emails/student.html'
        body = loader.render_to_string(email_template, make_context(obj))
    else:
        # Mail staff
        subject = 'Document Submissions Summary For Today'
        email_template = 'app/emails/staff.html'
        body = loader.render_to_string(email_template, make_context(obj=None, lst=lst))

    to = [user.email for user in User.objects.filter(usertype__user_type=user_type)]
    return {
          'subject': subject,
          'body': body,
          'to': to
        }

def send_email(subject, body, to):
    msg = EmailMultiAlternatives(subject, body, settings.FROM_EMAIL, to)
    msg.attach_alternative(body, 'text/html')

    msg.send()
