from django.shortcuts import render
from languagebits.models import Kana 
from languagebits.utils import * #to get random entries, quizes

# Create your views here.

# View details for a specififc function
# Returns kana details
def kana_detail(request, kana_id):
    kana  = get_kana_by_id(kana_id)
    text = kana.get_text()
    pronunciation = kana.get_pronunciation()
    kclass = kana.get_class_s()
    ktype = kana.get_type_s()
    return render(request, "languagebits/kana/detail.html", {'kana':kana, 'text':text, 'pronunciation':pronunciation})

# View details for a specififc function
# Returns word, furigana, romanji, definitions
def grammar_detail(request, grammar_id):
    grammar  = get_grammar_by_id(grammar_id)
    text = grammar.get_text()
    return render(request, "languagebits/grammar/detail.html", {'grammar':grammar, 'text':text})

#def vocabulary_detail(request, kana_id):
#    kana  = get_kana_by_id(kana_id)
#    text = kana.get_text()
#    pronunciation = kana.get_pronunciation()
#    kclass = kana.get_class_s()
#    ktype = kana.get_type_s()
#    return render(request, "languagebits/kana/detail.html", {'kana':kana, 'text':text, 'pronunciation':pronunciation})
