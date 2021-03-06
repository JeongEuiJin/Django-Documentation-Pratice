# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0006_auto_20170606_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TradInFo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('date_leaved', models.DateField(blank=True, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Player')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='players',
            field=models.ManyToManyField(through='introduction_to_models.TradInFo', to='introduction_to_models.Player'),
        ),
    ]
