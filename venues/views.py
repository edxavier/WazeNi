# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import VenueCreateForm
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.template import RequestContext
from .models import Venue, Category

# Create your views here.


class Home(ListView):
    paginate_by = 2
    model = Venue
    template_name = 'home.html'
    context_object_name = 'venues'
    queryset = Venue.objects.all().order_by('mapped')
    """
    def get(self, request, *args, **kwargs):
        venues = Venue.objects.all().order_by('mapped')
        return render(request, "home.html", locals())
    """


class CreateVenue(CreateView):
    model = Venue
    #fields = ['name', 'secondary_names', 'description', 'categories', 'position', 'phone_number', 'web', 'schedules']
    success_url = '/'
    form_class = VenueCreateForm
    template_name = "create_venue.html"


class UpdateVenue(UpdateView):
    model = Venue
    fields = ['mapped']
    success_url = '/'
    template_name = "mapped_venue.html"