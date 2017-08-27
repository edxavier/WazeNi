# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import VenueCreateForm
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.shortcuts import render
from django.template import RequestContext
from .models import Venue, Category, User

# Create your views here.


class Home(ListView):
    paginate_by = 10
    model = Venue
    template_name = 'home.html'
    context_object_name = 'venues'
    queryset = Venue.objects.all().order_by('status')
    """
    def get(self, request, *args, **kwargs):
        venues = Venue.objects.all().order_by('mapped')
        return render(request, "home.html", locals())
    """


class Resume(TemplateView):
    def get(self, request, *args, **kwargs):
        venues = Venue.objects.all().count()
        mapped = Venue.objects.filter(status=2).count()
        mapped_by_me = Venue.objects.filter(mapped_by=request.user, status=2).count()
        users = User.objects.all().count()
        editors = User.objects.filter(groups__name='editores').count()

        return render(request, "resume.html", locals())


class MyVenues(ListView):
    paginate_by = 10
    model = Venue
    template_name = 'home.html'
    context_object_name = 'venues'
    queryset = Venue.objects.all().order_by('status')

    def get(self, request, *args, **kwargs):
        venues = Venue.objects.filter(created_by=request.user).order_by('status')
        return render(request, "my_venues.html", locals())



class CreateVenue(CreateView):
    model = Venue
    #fields = ['name', 'secondary_names', 'description', 'categories', 'position', 'phone_number', 'web', 'schedules']
    success_url = '/'
    form_class = VenueCreateForm
    template_name = "create_venue.html"


class UpdateVenue(UpdateView):
    model = Venue
    fields = ['status', 'mapped_by', 'status_desc']
    success_url = '/'
    template_name = "mapped_venue.html"


class UpdateVenue2(UpdateView):
    model = Venue
    form_class = VenueCreateForm
    success_url = '/'
    template_name = "create_venue.html"