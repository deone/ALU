# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 12:11
from __future__ import unicode_literals

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_document_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=app.models.get_upload_path),
        ),
    ]