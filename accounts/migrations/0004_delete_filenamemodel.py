# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_authuser_is_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileNameModel',
        ),
    ]
