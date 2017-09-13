from django.conf.urls import url
from . import views

app_name = 'userinfo'
urlpatterns = [
    # ex: /userinfo/
    url(r'^$', views.profile, name='profile'), #view profile
    url(r'view', views.profile, name='profile'), #view profile
    url(r'update', views.update, name='update'), #update profile
    url(r'statistics', views.statistics, name='statistics'), #view login statistics
    # TODO: url(r'entrystats/(?P<sid>[0-9]+)/correct$', views.correct, name='correct'),
    # TODO: url(r'entrystats/(?P<sid>[0-9]+)/incorrect$', views.incorrect, name='incorrect'),
    # TODO: url(r'entrystats/(?P<sid>[0-9]+)/addnote$', views.add_note, name='add_note'),


]
