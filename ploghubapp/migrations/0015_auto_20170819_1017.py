# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ploghubapp', '0014_auto_20170819_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpost',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
