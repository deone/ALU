from django.contrib import admin

from .models import *

admin.site.register(UserType)
admin.site.register(Student)
admin.site.register(Announcement)
admin.site.register(DocumentType)
admin.site.register(DocumentRequest)
admin.site.register(Document)
