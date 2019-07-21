from languagebits.models import Kana, GrammarEntry, KanjiEntry, Vocabulary, LangDefinition
from languagestats.models import *
from userinfo.models import *
from random import *
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
import re
#from collections import namedtuple


#Replacement heuristics
a1 = ('あ', 'お')
a2 = ('い', 'え')
a3 = ('う', 'お')
a4 = ('え', 'い')
a5 = ('お', 'あ')

k1 = ("か", "が" )
k2 = ("き", "ぎ" )
k3 = ("く", "ぐ" )
k4 = ("け", "げ" )
k5 = ("こ", "ご" )

g1 = ("が", "か")
g2 = ("ぎ", "き")
g3 = ("ぐ", "く")
g4 = ("げ", "け")
g5 = ("げ", "ご")
	
s1 = ("さ", "ざ")
s2 = ("し", "じ")
s3 = ("す", "ず")
s4 = ("せ", "ぜ")
s5 = ("そ", "ぞ")

z1 = ("ざ", "さ")
z2 = ("じ", "し")
z3 = ("ず", "す")
z4 = ("ぜ", "せ")
z5 = ("ぞ", "そ")
	
t1 = ("た", "だ")
t2 = ("ち", "ぢ")
t3 = ("つ", "づ")
t4 = ("て", "で")
t5 = ("と", "ど")

ts1 = ("だ", "た")
ts2 = ("ぢ", "ち")
ts3 = ("づ", "つ")
ts4 = ("で", "て")
ts5 = ("ど", "と")
	
n1 = ("な", "ね")
n2 = ("に",  "ね")
n3 = ("ぬ", "の")
n4 = ("ね","に")
n5 = ("の","ぬ")
	
h1 = ("は", "ば")
h2 = ("ひ","び")
h3 = ("ふ","ぶ")
h4 = ("へ","べ")
h5 = ("ほ","ぼ")

b1 = ("ば", "ぱ")
b2 = ("び", "ぴ")
b3 = ("ぶ", "ぷ")
b4 = ("べ", "ぺ")
b5 = ("ぼ", "ぽ")

p1 = ("ぱ", "ば")
p2 = ("ぴ", "び")
p3 = ("ぷ", "ぶ")
p4 = ("ぺ", "べ")
p5 = ("ぽ", "ぼ")
	
m1 = ("ま","も")
m2 = ("み","め")
m3 = ("む","も")
m4 = ("め","み")
m5 = ("も","ま")
	
y1 = ("や", "よ")
y2 = ("ゆ", "よ")
y3 = ("よ", "や")

r1 = ("ら", "れ")
r2 = ("り", "れ")
r3 = ("る", "ろ")
r4 = ("れ", "ら")
r5 = ("ろ", "る")

w1 = ("わ", "を")
w2 = ("ゐ", "ゑ")
w3 = ("ゑ", "ゐ")
w4 = ("を", "わ")

SRULES =[a1, a2, a3, a4, a5, k1, k2, k3, k4, k5, g1, g2, g3, g4, g5, s1, s2, s3, s4, s5, z1, z2, z3, z4, z5, t1, t2, t3, t4, t5, ts1, ts2, ts3, ts4, ts5, n1, n2, n3, n4, n5, h1, h2, h3, h4, h5, b1, b2, b3, b4, b5, p1, p2, p3, p4, p5, m1, m2, m3, m4, m5, y1, y2, y3, r1, r2, r3, r4, r5, w1, w2, w3, w4 ]


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

#Function: get_vocab_by_id():
#Get a specififc vocabulary entry based on an id (pk=grammar_id)
def get_vocab_by_id(vocab_id):
    try:
        vocab = Vocabulary.objects.get(pk=vocab_id)
    except Vocabulary.DoesNotExist:
        raise Http404("Gomenazai~~~ VocabEntry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return vocab

#Function: get_random_entry()
#Get a random entry from dictionary
def get_random_vocab():
    vocab = None

    #loop until we get a valid entry
    while ( vocab == None ) :
        vocab_id = randint(1, 1500) #TODO : LANG_LEVEL.num_vocab Create a JLPT Category scoreboard? number of entries per jlpt level/level ?
        try:
            vocab = Vocabulary.objects.get(pk=vocab_id)
        except Vocabulary.DoesNotExist:
            vocab == None

    return vocab

#Function: get_random_entry()
#Get a random entry from dictionary
def get_random_definition():
    definition = None

    #loop until we get a valid entry
    while ( definition == None ) :
        definition_id = randint(1, 2000) #TODO: LANG_LEVEL.num_definitions: create a definitions scoreboard
        try:
            definition = LangDefinition.objects.get(pk=definition_id)
        except LangDefinition.DoesNotExist:
            definition == None

    return definition.entext

#Function: get_kanji_by_id():
#Get a specififc entry based on seqid (iseq_id=kanji_id)
def get_kanji_by_id(kanji_id):
    try:
        kanji = KanjiEntry.objects.get(seqid=kanji_id)
    except KanjiEntry.DoesNotExist:
        raise Http404("Gomenazai~~~ KanjiEntry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return kanji

#Function: get_kanjilist_by_jlpt():
#Get a list of all KanjiEntry based on JLPT N Level (jlpt=jlpt_level)
def get_kanjilist_by_jlpt(jlpt_level):
    try:
        kanjilist = KanjiEntry.objects.all().filter(jlptlevel=jlpt_level) 
    except KanjiEntry.DoesNotExist:
        raise Http404("Gomenazai~~~ KanjiEntry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return kanjilist

#Get a furigana entry and scramble 1 of the syllables 
def scramble_furigana(furigana):
    furigana2 = furigana
	
    #Replace K for G
    for str1, str2 in SRULES:
        if str1 in furigana :
            furigana2 = furigana.replace(str1, str2, 1)
            replaced = 1
            return furigana2


def get_vocab_stats(puser, vocab):
    #try to get the user profile TODO: should we try getting multiple times?
    try:
        vocabstats = VocabStats.objects.get(entry = vocab)
    except VocabStats.DoesNotExist: #if does not exist create a new one
        vocabstats = VocabStats(entry  = vocab)
        vocabstats.user = puser #TODO add to NEW)TERM memory
        vocabstats.seqid = vocab.seqid
        vocabstats.jlpt = vocab.jlpt
        vocabstats.text = vocab.text
        vocabstats.furigana = vocab.furigana
        vocabstats.add_date =  datetime.datetime.now()
        vocabstats.last_read_date = datetime.datetime.now()
        vocabstats.last_quiz_date = datetime.date(1978, 8, 16) #blank=true
        vocabstats.times_read = 0
        vocabstats.times_quized = 0
        vocabstats.furigana_score  = 0
        vocabstats.pronunciation_score  = 0
        vocabstats.definition_score  = 0
        vocabstats.save()
        #vocabstats.save()
    #Update vocab stats
    vocabstats.text = vocab.text
    times_read = vocabstats.times_read + 1
    vocabstats.times_read = times_read 

    if vocabstats.times_read > 30 and vocabstats.times_quized > 12:
        memory = get_long_term_mem(puser)
    elif vocabstats.times_read > 20 and  vocabstats.times_quized > 6:
        memory = get_mid_term_mem(puser)
    elif vocabstats.times_read > 3 :
        memory = get_short_term_mem(puser)
    else:
        memory = get_new_term_mem(puser)

    vocabstats.memory.clear() #remove previous items
    vocabstats.memory.add(memory)
    print("MEMORIES: %s" % vocabstats.memory.all())
    vocabstats.save()

    #print("Times read: %s" % (vocabstats.times_read) )
    print('MEMORY: %s Entry:%s [%s] : JLPT LEVEL:%s LEVEL:%s Times Read: %s (User: vocabstats.user:%s)' % (memory , vocabstats.text, vocabstats.furigana, vocabstats.jlpt , vocab.level, vocabstats.times_read, vocabstats.user  )  )
    return vocabstats

def get_new_term_mem(puser):
    try:
        memory = puser.memory_set.get(mem_type = NEW_TERM)
    except Memory.DoesNotExist: 
        memory = Memory(user = puser)
        memory.mem_type = NEW_TERM
        memory.save()
    return memory

def get_mem_random_vocab(puser, memory):
    length = 0
    vocab = None
    vocabstats_set = None
    vocabstats_set = memory.vocabstats_set.all()

    if vocabstats_set != None :
        length = len(vocabstats_set)

    if length == 0 : 
        vocabstats = None
        vocab = None
        return vocab, vocabstats
    else: 
        index = randint(0, length-1) 
        vocabstats = vocabstats_set[index]
        vocab = vocabstats.entry
        return vocab, vocabstats


def get_short_term_mem(puser):
    try:
        memory = puser.memory_set.get(mem_type = SHORT_TERM)
    except Memory.DoesNotExist: 
        memory = Memory(user = puser)
        memory.mem_type = SHORT_TERM
        memory.save()
    return memory

def get_mid_term_mem(puser):
    try:
        memory = puser.memory_set.get(mem_type = MID_TERM)
    except Memory.DoesNotExist: 
        memory = Memory(user = puser)
        memory.mem_type = MID_TERM
        memory.save()
    return memory

def get_long_term_mem(puser):
    try:
        memory = puser.memory_set.get(mem_type = LONG_TERM)
    except Memory.DoesNotExist: 
        memory = Memory(user = puser)
        memory.mem_type = LONG_TERM
        memory.save()
    return memory

#Simple Quiz Object to populate
class QuizObject:
    vocab = None
    vocab_stats = None
    seq_id = 55555555
    text = ""
    furigana = ""
    is_def = True
    mem_type = ""
    option1 = "" 
    option2 = ""
    option3 = ""
