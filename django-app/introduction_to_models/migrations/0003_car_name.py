# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0002_auto_20170606_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
