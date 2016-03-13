from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from django_comments.models import BaseCommentAbstractModel, COMMENT_MAX_LENGTH

class SimpleComment(BaseCommentAbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField(max_length=COMMENT_MAX_LENGTH)
    submit_date = models.DateTimeField(default=timezone.now)
