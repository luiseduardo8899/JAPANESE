from django.shortcuts import render
from django.http import JsonResponse
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
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0)
    definition2 = vocab.get_definition(1)
    return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text,  'furigana':furigana,  'definition':definition, 'definition2':definition2})

# Returns vocabulary details based on ID (TODO: use seqid)
def vocab_stats_detail(request, vocab_id):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_vocab_by_id(vocab_id)
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0)
    definition2 = vocab.get_definition(1)
    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)
    return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, "vocabstats":vocabstats, 'next':"/language/vocab/random_stats_view/"})

# Returns vocabulary details based on ID (TODO: use seqid)
def check_def_answer(request, vocab_id):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_vocab_by_id(vocab_id)
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0)
    definition2 = vocab.get_definition(1)
    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)

    answer_definition = request.GET.get('definition', False)

    if answer_definition != False:
        if answer_definition == definition or answer_definition == definition2:
            vocabstats.quiz_def_correct()
            print("CORRECT DEFINITION: %s Times Quized: %s Score: %s" % (answer_definition, vocabstats.times_quized,  vocabstats.definition_score))
            return JsonResponse({"success": True, "result":True, "score":vocabstats.definition_score, "times_quized":vocabstats.times_quized})
        else:
            vocabstats.quiz_def_incorrect()
            print("X WRONG X DEFINITION: %s Times Quized: %s Score: %s" % (answer_definition, vocabstats.times_quized,  vocabstats.definition_score))
            return JsonResponse({"success": True, "result":False, "score":vocabstats.definition_score+1, "times_quized":vocabstats.times_quized})
    else:
            return JsonResponse({"success": False, "result":False})
    #return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, "vocabstats":vocabstats, 'next':"/language/vocab/random_stats_view/"})

# Returns vocabulary details based on ID (TODO: use seqid)
def check_fur_answer(request, vocab_id):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')

    vocab  = get_vocab_by_id(vocab_id)
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)

    answer_furigana = request.GET.get('furigana', False)

    if answer_furigana != False:
        if answer_furigana == furigana:
            vocabstats.quiz_fur_correct()
            print("CORRECT FURIGANA: %s Times Quized: %s Furigana Score: %s" % (answer_furigana, vocabstats.times_quized,  vocabstats.furigana_score))
            return JsonResponse({"success": True, "result":True, "furigana_score":vocabstats.furigana_score, "times_quized":vocabstats.times_quized})
        else:
            vocabstats.quiz_fur_incorrect()
            print("X INCORRECT * FURIGANA: %s Times Quized: %s Furigana Score: %s" % (answer_furigana, vocabstats.times_quized,  vocabstats.furigana_score))
            return JsonResponse({"success": True, "result":False, "furigana_score":vocabstats.furigana_score, "times_quized":vocabstats.times_quized})
    else:
            return JsonResponse({"success": False, "result":False})

# Returns a random vocabulary/verb/or grammar pattern which the users hould be studying
def next_steps(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')

    return render(request, "languagebits/vocab/next_steps.html")

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


# Returns a random vocabulary/verb/or grammar pattern which the users hould be studying
def random_stats_view(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')
    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0)
    definition2 = vocab.get_definition(1)
    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)
    return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, "vocabstats":vocabstats, 'next':"/language/vocab/random_stats_view/"})
    #return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2})




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

    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)
    return render(request, "languagebits/vocab/definition_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, 'definition3':definition3, "vocabstats":vocabstats})

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

    return render(request, "languagebits/vocab/furigana_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'furigana2':furigana2, "vocabstats":vocabstats})

def long_term_memory(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/long_term_memory/')

    memory = get_long_term_mem(request.user)
    vocabstats_set = memory.vocabstats_set.all()
    print("MID TERM MEMORY : %s" % vocabstats_set)
    return render(request, "languagebits/vocab/memory_detail.html", {'vocabstats_set':vocabstats_set})

def mid_term_memory(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/mid_term_memory/')

    memory = get_mid_term_mem(request.user)
    vocabstats_set = memory.vocabstats_set.all()
    print("MID TERM MEMORY : %s" % vocabstats_set)
    return render(request, "languagebits/vocab/memory_detail.html", {'vocabstats_set':vocabstats_set})

def short_term_memory(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/short_term_memory/')

    memory = get_short_term_mem(request.user)
    vocabstats_set = memory.vocabstats_set.all()
    print("SHORT TERM MEMORY : %s" % vocabstats_set)
    return render(request, "languagebits/vocab/memory_detail.html", {'vocabstats_set':vocabstats_set})


def practice(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/practice/')

    vocab  = get_random_vocab()
    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0) #definition is always correct answer

    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)

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

        return render(request, "languagebits/vocab/detail.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, "vocabstats":vocabstats, 'next':"/language/vocab/practice/"})
    elif is_def_quiz == 1:
        definition2 = get_random_definition()
        definition3 = get_random_definition()

        return render(request, "languagebits/vocab/definition_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'definition2':definition2, 'definition3':definition3, "vocabstats":vocabstats,  'next':"/language/vocab/practice/"})
    else:
        furigana2 = scramble_furigana(furigana)
        return render(request, "languagebits/vocab/furigana_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'definition':definition, 'furigana2':furigana2, "vocabstats":vocabstats, 'next':"/language/vocab/practice/"})


#Spaced repetition practice
def spaced_practice(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/spaced_practice/')

    vocab = None
    puser = request.user

    DEF_QUIZ_PROB = 0
    FUR_QUIZ_PROB = 0
    mem_type = 0 #0:NEW 1:SHORT, 2:MID 3:LONG
    #NOTE: DEF_QUIZ_PROB + FUR_QUIZ_PROB should add up to be < 100

    while (vocab == None):
        rand_num = random.randint(1,101)
        #50% chance  get a new word to practice
        if rand_num < 20:
            memory = get_new_term_mem(puser)
            vocab, vocabstats  = get_mem_random_vocab(puser, memory)
            QUIZ_PROB = 0
            FUR_QUIZ_PROB = 0
            mem_type = 0
        #30% chance  get a short term memory word  to practice
        elif rand_num < 90:
            memory = get_short_term_mem(puser)
            vocab, vocabstats  = get_mem_random_vocab(puser, memory)
            if vocabstats.times_read > 20 :
                DEF_QUIZ_PROB = 61
                FUR_QUIZ_PROB = 36
            else:
                DEF_QUIZ_PROB = 55
                FUR_QUIZ_PROB = 35
            mem_type = 1
    #15% chance  get a mid term memory word  to practice
        elif rand_num < 95:
            memory = get_mid_term_mem(puser)
            vocab, vocabstats  = get_mem_random_vocab(puser, memory)
            DEF_QUIZ_PROB = 40
            FUR_QUIZ_PROB = 30
            mem_type = 2
    #5% chance  get a mid term memory word  to practice
        else:
            memory = get_long_term_mem(puser)
            vocab, vocabstats  = get_mem_random_vocab(puser, memory)
            DEF_QUIZ_PROB = 50
            FUR_QUIZ_PROB = 40
            mem_type = 3

    #if new_words < 10  add a random new word
    #vocab  = get_random_vocab() TODO: add random vocab entry to memory

    text = vocab.get_text()
    furigana = vocab.get_furigana()
    #Get definitions:
    definition = vocab.get_definition(0) #definition is always correct answer

    #get existing stats or create new ones
    vocabstats  = get_vocab_stats(request.user, vocab)

    is_vocab = 0
    is_def_quiz = 0
    is_fur_quiz = 0
    rand_num = random.randint(1,101) 
    rand_num2 = random.randint(1,101) 

    if rand_num < DEF_QUIZ_PROB:
        is_def_quiz = 1
    elif rand_num2 < FUR_QUIZ_PROB:
        is_fur_quiz = 1
    else:
        is_vocab = 1

    if is_vocab == 1 :
        definition2 = vocab.get_definition(1)

        return render(request, "languagebits/vocab/detail_practice.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'mem_type':mem_type, 'definition':definition, 'definition2':definition2, "vocabstats":vocabstats, 'next':"/language/vocab/spaced_practice/"})
    elif is_def_quiz == 1:
        definition2 = get_random_definition()
        definition3 = get_random_definition()

        return render(request, "languagebits/vocab/definition_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana, 'mem_type':mem_type, 'definition':definition, 'definition2':definition2, 'definition3':definition3, "vocabstats":vocabstats,  'next':"/language/vocab/spaced_practice/"})
    else:
        furigana2 = scramble_furigana(furigana)
        return render(request, "languagebits/vocab/furigana_quiz.html", {'entry':vocab, 'text':text, 'furigana':furigana,  'mem_type':mem_type, 'definition':definition, 'furigana2':furigana2, "vocabstats":vocabstats, 'next':"/language/vocab/spaced_practice/"})


#Spaced repetition practice 100
def spaced_quiz_100(request):
    # Redirect to Homepage if user is not signed in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/?next=/language/vocab/spaced_practice/')


    quiz_q = []

    puser = request.user
    user_stats = get_stats(puser)

    DEF_QUIZ_PROB = 0
    FUR_QUIZ_PROB = 0
    mem_type = 0 #0:NEW 1:SHORT, 2:MID 3:LONG

    #Collect up to N quizes
    while ( len(quiz_q) < 5 ):
        vocab = None
        #NOTE: DEF_QUIZ_PROB + FUR_QUIZ_PROB should add up to be < 100
        while (vocab == None):
            rand_num = random.randint(1,101)
            #90% chance  get a short term memory word  to practice
            if rand_num < 90:
                memory = get_short_term_mem(puser)
                vocab, vocabstats  = get_mem_random_vocab(puser, memory)
                if vocabstats.times_read > 20 :
                    DEF_QUIZ_PROB = 61
                    FUR_QUIZ_PROB = 36
                else:
                    DEF_QUIZ_PROB = 55
                    FUR_QUIZ_PROB = 35
                mem_type = 1
        #15% chance  get a mid term memory word  to practice
            elif rand_num < 95:
                memory = get_mid_term_mem(puser)
                vocab, vocabstats  = get_mem_random_vocab(puser, memory)
                DEF_QUIZ_PROB = 40
                FUR_QUIZ_PROB = 30
                mem_type = 2
        #5% chance  get a mid term memory word  to practice
            else:
                memory = get_long_term_mem(puser)
                vocab, vocabstats  = get_mem_random_vocab(puser, memory)
                DEF_QUIZ_PROB = 50
                FUR_QUIZ_PROB = 40
                mem_type = 3

        #if new_words < 10  add a random new word
        #vocab  = get_random_vocab() TODO: add random vocab entry to memory

        text = vocab.get_text()
        furigana = vocab.get_furigana()
        #Get definitions:
        definition = vocab.get_definition(0) #definition is always correct answer

        #get existing stats or create new ones
        vocab_stats  = get_vocab_stats(request.user, vocab)

        is_vocab = 0
        is_def_quiz = 0
        is_fur_quiz = 0
        rand_num = random.randint(1,101) 
        rand_num2 = random.randint(1,101) 

        if rand_num < DEF_QUIZ_PROB:
            is_def_quiz = 1
        elif rand_num2 < FUR_QUIZ_PROB:
            is_fur_quiz = 1
        else:
            is_def_quiz = 1

        if is_def_quiz == 1:
            def_quiz = QuizObject()
            definition2 = get_random_definition()
            definition3 = get_random_definition()
            #Form quiz object
            def_quiz.vocab = vocab
            def_quiz.vocab_stats = vocab_stats
            def_quiz.seqid = vocab.seqid
            def_quiz.text = text
            def_quiz.furigana = furigana
            def_quiz.is_def = True
            def_quiz.mem_type = mem_type
            def_quiz.option1 = definition 
            def_quiz.option2 = definition2
            def_quiz.option3 = definition3
            quiz_q.append(def_quiz)
            print("Added a definition quiz: %s" % def_quiz )

        else:
            fur_quiz = QuizObject()
            furigana2 = scramble_furigana(furigana)
            #Form quiz object
            fur_quiz.vocab = vocab
            fur_quiz.vocab_stats = vocab_stats
            fur_quiz.seqid = vocab.seqid
            fur_quiz.text = text
            fur_quiz.furigana =  ""
            fur_quiz.is_def = False
            fur_quiz.mem_type = mem_type
            fur_quiz.option1 = furigana 
            fur_quiz.option2 = furigana2
            quiz_q.append(fur_quiz)
            print("Added a furigana quiz: %s" % fur_quiz )

    return render(request, "languagebits/vocab/spaced_quiz_100.html", {'quiz_q':quiz_q,  'next':"/language/vocab/all_done_100"})

