from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Common(models.Model):
    slug = models.SlugField(unique=True, editable=False)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
    

class Category(Common):
    name = models.CharField(max_length=50)

class Topic(Common):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
