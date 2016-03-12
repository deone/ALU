from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from utils import AutoSlugField

class Common(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", db_index=False, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
    

class Category(Common):
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Topic(Common):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
