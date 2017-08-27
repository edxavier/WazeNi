"""waze_poi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from waze_poi import settings
from django.conf.urls.static import static
from venues.views import Home, CreateVenue, UpdateVenue, UpdateVenue2, MyVenues, Resume
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^my_venues$', MyVenues.as_view(), name='my_venues'),
    url(r'^resume', Resume.as_view(), name='resume'),
    url(r'^venue/new$', CreateVenue.as_view(), name='create_venue'),
    url(r'^venue/(?P<pk>[0-9]+)/$', UpdateVenue.as_view(), name='update_venue'),
    url(r'^my_venue/(?P<pk>[0-9]+)/$', UpdateVenue2.as_view(), name='update_venue2'),

    url(r'^admin/', admin.site.urls),
    url(r'^select2/', include('django_select2.urls')),
    url('', include('social_django.urls', namespace='social')),
    url('^logout/$', auth_views.logout_then_login, name='logout'),

]

