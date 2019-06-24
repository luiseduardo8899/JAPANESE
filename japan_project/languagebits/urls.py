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
    url(r'^vocab/(?P<vocab_id>[0-9]+)/$', views.vocab_detail, name='vocab_detail'),
    url(r'^vocab/stats/(?P<vocab_id>[0-9]+)/$', views.vocab_stats_detail, name='vocab_stats_detail'),
    url(r'^vocab/check_def_answer/(?P<vocab_id>[0-9]+)/$', views.check_def_answer, name='check_def_answer'),
    url(r'^vocab/check_fur_answer/(?P<vocab_id>[0-9]+)/$', views.check_fur_answer, name='check_fur_answer'),

    url(r'^vocab/flashcards/$', views.flashcards, name='flashcards'),
    url(r'^vocab/random_stats_view/$', views.random_stats_view, name='random_stats_view'),
    url(r'^vocab/definition_quiz/$', views.definition_quiz, name='definition_quiz'),
    url(r'^vocab/furigana_quiz/$', views.furigana_quiz, name='furigana_quiz'),
    url(r'^vocab/practice/$', views.practice, name='practice'),
    url(r'^vocab/short_term_memory/$', views.short_term_memory, name='short_term_memory'),
    url(r'^vocab/mid_term_memory/$', views.mid_term_memory, name='mid_term_memory'),
    url(r'^vocab/long_term_memory/$', views.long_term_memory, name='long_term_memory'),
]
