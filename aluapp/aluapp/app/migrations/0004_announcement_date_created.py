# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]