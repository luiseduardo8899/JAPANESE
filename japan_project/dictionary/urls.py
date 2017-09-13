from django.conf.urls import url
from . import views

app_name = 'dictionary'
urlpatterns = [
    # ex: /dictionary/
    url(r'^(?P<word_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^random/$', views.random, name='random'),

    # url(r'^$', views.random, name='random'), #TODO : add a splash page for dictionary
    # url(r'^list/$', views.entry_list, name='entry_list'),
    # url(r'^(?P<word_id>[0-9]+)/learn/$', views.learn, name='learn'),
    # url(r'^(?P<word_id>[0-9]+)/remove/$', views.remove, name='remove'),
    # url(r'^random_quiz/$', views.random_quiz, name='random_quiz'),
    # url(r'^(?P<word_id>[0-9]+)/quiz/$', views.quiz, name='quiz'),
]
