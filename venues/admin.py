# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Venue, User
# Register your models here.


@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    pass


@admin.register(Venue)
class VenueAdmin (admin.ModelAdmin):
    pass