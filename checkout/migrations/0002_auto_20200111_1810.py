# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-11 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town_or_city',
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=40),
        ),
    ]
