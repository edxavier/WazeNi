# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 16:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='mapped_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mapped_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
