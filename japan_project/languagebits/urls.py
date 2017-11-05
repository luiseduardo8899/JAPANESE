from django.conf.urls import url
from . import views

app_name = 'languagebits'
urlpatterns = [
    # ex: /languagebits/
    url(r'^kana/(?P<kana_id>[0-9]+)/$', views.kana_detail, name='kana_detail'),
    url(r'^grammar/(?P<grammar_id>[0-9]+)/$', views.grammar_detail, name='grammar_detail'),
    url(r'^kanji/jlpt/(?P<jlpt_level>[0-9]+)/$', views.kanji_list, name='kanji_list'),
    url(r'^kanji/(?P<kanji_id>[0-9]+)/$', views.kanji_detail, name='kanji_detail'),
    url(r'^grammar/(?P<grammar_id>[0-9]+)/$', views.grammar_detail, name='grammar_detail'),
]
