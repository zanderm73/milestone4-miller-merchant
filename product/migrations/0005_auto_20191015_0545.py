# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_product_decription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_decription',
            field=models.CharField(default='description', max_length=1000),
        ),
    ]
