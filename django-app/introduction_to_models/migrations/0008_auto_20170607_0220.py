# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0007_auto_20170606_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradinfo',
            name='prev_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='introduction_to_models.Club'),
        ),
        migrations.AddField(
            model_name='tradinfo',
            name='recommender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tradinfo_set_by_recommender', to='introduction_to_models.Player'),
        ),
    ]