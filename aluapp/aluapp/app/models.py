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
