# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-22 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0014_remove_bookreview_booknamevote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='active',
        ),
        migrations.RemoveField(
            model_name='bookreview',
            name='vote',
        ),
    ]
