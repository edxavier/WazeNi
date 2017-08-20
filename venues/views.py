# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import RequestContext
from .models import Venue, Category

# Create your views here.


class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        venues = Category.objects.all().order_by('name')
        return render(request, "home.html", locals())
