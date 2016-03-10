from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.title
