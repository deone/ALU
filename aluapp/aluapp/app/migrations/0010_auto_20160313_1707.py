# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 17:07
from __future__ import unicode_literals

from django.db import migrations
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160313_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='slug',
            field=utils.AutoSlugField(blank=True, db_index=False, editable=False, populate_from=b'title'),
        ),
        migrations.AlterField(
            model_name='documentrequest',
            name='slug',
            field=utils.AutoSlugField(blank=True, db_index=False, editable=False, populate_from=b'title'),
        ),
    ]