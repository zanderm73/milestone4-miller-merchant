# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-21 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0011_bookreview_monthwinner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='bookreview',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
