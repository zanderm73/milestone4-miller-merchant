# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-02 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0005_auto_20191117_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='bookofthemonth',
            field=models.CharField(default='no', max_length=5),
        ),
    ]
