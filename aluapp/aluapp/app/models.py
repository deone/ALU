from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class UserType(models.Model):
    TEACHER = 'TCH'
    STUDENT = 'STD'

    TYPE_CHOICES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )
    
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    index_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Announcement, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        pass
