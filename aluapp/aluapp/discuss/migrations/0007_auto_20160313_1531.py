# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0006_auto_20160313_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_submitted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
