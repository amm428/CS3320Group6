# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20161025_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipeList',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]