from languagebits.models import Kana, GrammarEntry
from random import *
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404

#Function: get_kana_by_id():
#Get a specififc entry based on an id (pk=kana_id)
def get_kana_by_id(kana_id):
    try:
        kana = Kana.objects.get(pk=kana_id)
    except Kana.DoesNotExist:
        raise Http404("Gomenazai~~~ KanaEntry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return kana

#Function: get_grammar_by_id():
#Get a specififc grammar entry based on an id (pk=grammar_id)
def get_grammar_by_id(grammar_id):
    try:
        grammar = GrammarEntry.objects.get(pk=grammar_id)
    except GrammarEntry.DoesNotExist:
        raise Http404("Gomenazai~~~ GrammarEntry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return grammar
