from django.shortcuts import render
from languagebits.models import Kana 
from languagebits.utils import * 

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

# Returns grammar details based on ID (TODO: use seqid)
def grammar_detail(request, grammar_id):
    grammar  = get_grammar_by_id(grammar_id)
    text = grammar.get_text()
    return render(request, "languagebits/grammar/detail.html", {'grammar':grammar, 'text':text})

# Returns KanjiEntry based on XML seqid 
def kanji_detail(request, kanji_id):
    kanji  = get_kanji_by_id(kanji_id)
    text = kanji.get_text()
    return render(request, "languagebits/kanji/detail.html", {'kanji':kanji, 'text':text})

# Returns KanjiList based on JLPT N level, and ordered by sublevel
def kanji_list(request, jlpt_level):
    kanjilist  = get_kanjilist_by_jlpt(jlpt_level)
    text = "Kanji List for JLPT N"+jlpt_level
    return render(request, "languagebits/kanji/list.html", {'kanjilist':kanjilist, 'text':text})

#def vocabulary_detail(request, kana_id):
#    kana  = get_kana_by_id(kana_id)
#    text = kana.get_text()
#    pronunciation = kana.get_pronunciation()
#    kclass = kana.get_class_s()
#    ktype = kana.get_type_s()
#    return render(request, "languagebits/kana/detail.html", {'kana':kana, 'text':text, 'pronunciation':pronunciation})
