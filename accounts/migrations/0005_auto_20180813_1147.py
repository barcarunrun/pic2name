# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_filenamemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('userID', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
