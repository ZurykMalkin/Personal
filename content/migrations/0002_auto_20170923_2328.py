# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='autor',
            field=models.CharField(max_length=30),
        ),
    ]
