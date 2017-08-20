# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=100)
    secondary_names = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    position = GeopositionField()
    web = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    schedules = models.TextField(null=True, blank=True)


    valet_parking = models.BooleanField(default=False)
    auto_service = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    restrooms = models.BooleanField(default=False)
    credit_cards = models.BooleanField(default=False)
    reservations = models.BooleanField(default=False)
    outdoor_seats = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    to_take_away = models.BooleanField(default=False)
    wheelchair_access = models.BooleanField(default=False)
    mapped = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Puntos'
        verbose_name = 'Punto'
        permissions = (
            ("set_mapped", "Puede actualizar el estado a mapeado"),
            ("can_export", "Puede exportar los lugares"),
        )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name