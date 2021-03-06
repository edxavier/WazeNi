# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_auto_20170827_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='denied_reason',
            new_name='status_desc',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='denied',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='mapped',
        ),
        migrations.AddField(
            model_name='venue',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Mapeado'), (3, 'Denegado')], default=1),
        ),
    ]
