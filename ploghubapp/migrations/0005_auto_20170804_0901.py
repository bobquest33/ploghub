# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ploghubapp', '0004_auto_20170803_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpost',
            name='body',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=20000),
        ),
    ]