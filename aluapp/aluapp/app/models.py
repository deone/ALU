from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from utils import AutoSlugField

class UserType(models.Model):
    STAFF = 'STF'
    STUDENT = 'STD'

    TYPE_CHOICES = (
        (STAFF, 'Staff'),
        (STUDENT, 'Student'),
    )
    
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'User Types'

class Student(models.Model):
    index_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


# These should be in another app
class Common(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    slug = AutoSlugField(populate_from="title", db_index=False, blank=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Announcement(Common):

    @models.permalink
    def get_absolute_url(self):
        return 'app:announcement', (self.id, self.slug,)

class DocumentType(models.Model):
    document_type = models.CharField(max_length=50)

    def __str__(self):
        return self.document_type

    class Meta:
        verbose_name_plural = 'Document Types'

class DocumentRequest(Common):
    document_type = models.ForeignKey(DocumentType)
    upload_quantity = models.PositiveSmallIntegerField('Number Of Files Allowed')

    @models.permalink
    def get_absolute_url(self):
        return 'app:document_request', (self.id, self.slug,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Document Requests'

class Document(models.Model):
    user = models.ForeignKey(User)
    document_request = models.ForeignKey(DocumentRequest)
    document = models.FileField()
    date_submitted = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "%s %s" % (self.user.get_full_name(), self.document_type.document_type)
