# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'permissions': (('set_mapped', 'Puede actualizar el estado a mapeado'), ('can_export', 'Puede exportar los lugares')), 'verbose_name': 'Punto', 'verbose_name_plural': 'Puntos'},
        ),
        migrations.AddField(
            model_name='venue',
            name='mapped',
            field=models.BooleanField(default=False),
        ),
    ]
