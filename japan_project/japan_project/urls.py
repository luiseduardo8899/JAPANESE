"""japan_project URL Configuration

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
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('allauth.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^premium/', include('premiumaccount.urls')),
    url(r'^teacher/', include('teacher.urls')),
    url(r'^userinfo/', include('userinfo.urls')),
    url(r'^dictionary/', include('dictionary.urls')),
    url(r'^language/', include('languagebits.urls')),
    url(r'^search/', include('haystack.urls')),
    #url(r'^hello/', views.hello, name='hello'), #TODO : add a splash page for dictionary
    #url(r'^byebye/', views.byebye, name='byebye'), #TODO : add a splash page for dictionary
    url(r'^$', RedirectView.as_view(url='/search/', permanent=False), name='index')
]
