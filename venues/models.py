# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.
from waze_poi.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar = models.URLField(null=True, blank=True)


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
    STATUS_CHOICES = (
        (1, ("Pendiente")),
        (2, ("Mapeado")),
        (3, ("Denegado")),
    )
    name = models.CharField(max_length=100)
    secondary_names = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    position = GeopositionField()
    web = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    schedules = models.TextField(null=True, blank=True)

    valet_parking = models.BooleanField(blank=True, default=False)
    auto_service = models.BooleanField(blank=True, default=False)
    wifi = models.BooleanField(blank=True, default=False)
    restrooms = models.BooleanField(blank=True, default=False)
    credit_cards = models.BooleanField(blank=True, default=False)
    reservations = models.BooleanField(blank=True, default=False)
    outdoor_seats = models.BooleanField(blank=True, default=False)
    air_conditioning = models.BooleanField(blank=True, default=False)
    parking = models.BooleanField(blank=True, default=False)
    delivery = models.BooleanField(blank=True, default=False)
    to_take_away = models.BooleanField(blank=True, default=False)
    wheelchair_access = models.BooleanField(blank=True, default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    status_desc = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL)
    mapped_by = models.ForeignKey(AUTH_USER_MODEL, related_name='mapped_by', null=True, blank=True)

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

    @property
    def get_position(self):
        return str(self.position.longitude) + ' ' + str(self.position.latitude)