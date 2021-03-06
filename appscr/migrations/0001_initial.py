# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('likes', models.PositiveIntegerField(null=True)),
                ('comments', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('top_count', models.PositiveIntegerField(default=None, null=True)),
                ('videos', models.NullBooleanField()),
            ],
        ),
    ]
