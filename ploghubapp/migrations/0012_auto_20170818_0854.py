# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ploghubapp', '0011_auto_20170816_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluserprofile',
            name='about',
            field=models.CharField(default='[empty]', max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(default='[empty]', max_length=1000),
        ),
    ]