from django.shortcuts import render
from languagebits.models import Kana 
from languagebits.models import Vocabulary 
from languagebits.utils import * 
from userinfo.utils import * #to get user profile and stats
import random

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

# Returns grammar details based on ID (TODO: use seqid)
def grammar_detail(request, grammar_id):
    grammar  = get_grammar_by_id(grammar_id)
    text = grammar.get_text()
    return render(request, "languagebits/grammar/detail.html", {'grammar':grammar, 'text':text})

# Returns vocabulary details based on ID (TODO: use seqid)
def vocab_detail(request, vocab_id):
    vocab  = get_vocab_by_id(vocab_id)
    kanji = vocab.get_text()
    furigana = vocab.get_furigana()
    def1 = vocab.get_definition()
    #def2 = vocab.get_def2()
    #def3 = vocab.get_def3()
    return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':kanji, 'definition':def1})

# Returns a random vocabulary/verb/or grammar pattern which the users hould be studying
def flashcards(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0)
    definition2 = vocab.get_definition(1)

    return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2})


# Returns a random vocabulary definition quiz
def definition_quiz(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0) #definition is always correct answer
    definition2 = get_random_definition()
    definition3 = get_random_definition()

    return render(request, "languagebits/vocab/definition_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, 'definition3':definition3})

# Returns a random furigana selection quiz
def furigana_quiz(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0) #definition is always correct answer
    furigana2 = scramble_furigana(furigana)

    return render(request, "languagebits/vocab/furigana_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'furigana2':furigana2})

def practice(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/practice/')

    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0) #definition is always correct answer

    is_vocab = 0
    is_def_quiz = 0
    is_fur_quiz = 0
    rand_num = random.randint(1,101) 
    #80% probability to get a practice word
    if rand_num < 81:
        is_vocab = 1
    #15% probability to get a definition quiz
    elif rand_num < 96:
        is_def_quiz = 1
    #5% probability to get a furigana quiz
    else:
        is_fur_quiz = 1

    if is_vocab == 1 :
        definition2 = vocab.get_definition(1)

        return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, 'next':"/language/vocab/practice/"})
    elif is_def_quiz == 1:
        definition2 = get_random_definition()
        definition3 = get_random_definition()

        return render(request, "languagebits/vocab/definition_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, 'definition3':definition3,  'next':"/language/vocab/practice/"})
    else:
        furigana2 = scramble_furigana(furigana)
        return render(request, "languagebits/vocab/furigana_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'furigana2':furigana2, 'next':"/language/vocab/practice/"})
