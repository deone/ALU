# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_no', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(choices=[(b'TCH', b'Teacher'), (b'STD', b'Student')], max_length=3),
        ),
    ]
