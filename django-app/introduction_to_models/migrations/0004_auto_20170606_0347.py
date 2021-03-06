# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0003_car_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.CharField(choices=[('studnet', '학생'), ('teacher', '선생')], default='studnet', max_length=10, verbose_name='유형'),
        ),
        migrations.AddField(
            model_name='person',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Person'),
        ),
    ]
