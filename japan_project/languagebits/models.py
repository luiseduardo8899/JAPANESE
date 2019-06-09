from django.db import models
from django.utils import timezone
#from videos.models import Video
import datetime

#Integer definition of JLPT_N levels
JLPT_N5 = 5
JLPT_N4 = 4
JLPT_N3 = 3
JLPT_N2 = 2
JLPT_N1 = 1
JLPT_N1P = 0 #More advanced than material covered in JLPT_N1
JLPT_LEVELS = (
    (JLPT_N5, "JLPT_N5"),
    (JLPT_N4, "JLPT_N4"),
    (JLPT_N3, "JLPT_N3"),
    (JLPT_N2, "JLPT_N2"),
    (JLPT_N1, "JLPT_N1"),
    (JLPT_N1P, "JLPT_N1P")
)

KATAKANA = 1
HIRAGANA = 0 
KANA_CLASS = (
    (KATAKANA, "KATAKANA"),
    (HIRAGANA, "HIRAGANA")
)

DAKUTEN = 2
COMBO = 1
BASE = 0 #More advanced than material covered in JLPT_N1
KANA_TYPE = (
    (DAKUTEN, "DAKUTEN"),
    (COMBO, "COMBO"),
    (BASE, "BASE")
)

#TODO: Define Verb Types :TODO:
RU_VERB = 0 #
U_VERB = 1
G5_VERB = 2 #GO DAN Verb ...

#Part of speech items used in Japanese Grammar
TBD = 0
NOUN = 1
VERB = 2
I_ADJ = 3
NA_ADJ = 4

POS_ITEMS = (
    (NOUN, "NOUN"),
    (VERB, "VERB"),
    (I_ADJ, "I_ADJ"),
    (NA_ADJ, "NA_ADJ")
    #TODO do full ist of vocabulary items...
)

#Grammar Modifiers used in common Japanese Grammar Patterns
PLUS = 1000
MINUS = 1001
IxKU = 1002
NAxNI = 1003

MODIFIER_ITEMS = (
    (PLUS, "PLUS"),	#Concatenate the following word to the string before it
    (MINUS, "MINUS"),   #Remove the following string from the end of the string before it
    (IxKU, "IxKU"),	#Change the ending "i" in a word to a "ku"
    (NAxNI, "NAxNI"),	#Change the ending "na" in a word to a "ni"
)

ALL_ITEMS = POS_ITEMS + MODIFIER_ITEMS

#Class Level: 
#Defines a level of study, used to match a language entry
#to a specific level of study. Used to track student progress 
#and collect the right vocabulary and quizes to present to student.
#there may be more than one entry of Level with the same level number
class Level(models.Model): 
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)     #level of difficulty (0-4095) : 4K levels
    def __str__(self):
        return self.name


#Class Kana (level 0)
#Defines Hiragana and Katakana reading entries
class Kana(models.Model): 
    seqid = models.IntegerField(default=0) #TODO: make this a single *key*
    text = models.CharField(max_length=12)
    pronunciation = models.CharField(max_length=12)
    kanaclass = models.IntegerField(choices=KANA_CLASS, default=0)
    kanatype = models.IntegerField(choices=KANA_TYPE, default=0)
    description = models.CharField(max_length=200, default=" ")

    def __str__(self):
        return self.text

    def get_text(self):
        return self.text

    def get_pronunciation(self):
        return self.pronunciation

    def get_class_s(self):
        if self.kanaclass == HIRAGANA:
            return "Hiragana"
        else:
            return "Katakana"

    def get_type_s(self):
        if self.kanatype == DAKUTEN:
            return "Dakuten"
        if self.kanatype == COMBO:
            return "Combo"
        else:
            return "Base"

#Class Kanji
#Defines single Kanji character, and reading types
class KanjiEntry(models.Model): 
    seqid = models.IntegerField(default=0) #TODO: make this a single *key*
    svgid = models.IntegerField(default=0) #this key should match SVGKanji ID
    name = models.CharField(max_length=140)
    text = models.CharField(max_length=12)
    jlpt = models.IntegerField(choices=JLPT_LEVELS, default=5)
    level = models.IntegerField(default=0) # Total of 1-1024

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

class Kunyomi(models.Model):
    text = models.CharField(max_length=12)
    entry = models.ManyToManyField(KanjiEntry) # After creating object,  use kunyomi.add(<KanjiEntry pointer>)

    def __str__(self):
        return "Kunyomi: " + self.text

class Onyomi(models.Model):
    text = models.CharField(max_length=12)
    entry = models.ManyToManyField(KanjiEntry) # After creating object,  use onyomi.add(<KanjiEntry pointer>)

    def __str__(self):
        return "Onyomi: " + self.text

class KanjiDescription(models.Model):
    text = models.CharField(max_length=200)
    entry = models.ManyToManyField(KanjiEntry) # After creating object,  use kanjidescription.add(<KanjiEntry pointer>)

    def __str__(self):
        return "KanjiDescription: " + self.text


#A GrammarPattern can contain multiple PatternFormula entries
class GrammarEntry(models.Model):
    seqid = models.IntegerField(default=0)
    text = models.CharField(max_length=140)
    jlpt = models.IntegerField(choices=JLPT_LEVELS, default=5)
    level = models.IntegerField(default=0) # Total of 1-1024
    summary =  models.CharField(max_length=250) #Simple definition, for entire entry look to dictionary entry definitions
    #TODO: How to proerly capture exeptions? TODO

    def get_text(self):
        return self.text

    def __str__(self):
        return "GrammarEntry#%s" % self.text

class GrammarDescription(models.Model):
    text = models.CharField(max_length=2000) #pitem.name = "I-adjective + naru"
    entry = models.ManyToManyField(GrammarEntry) # After creating object,  use grammarpattern.add(<PatternFormula pointer>)
    def __str__(self):
        return "PatternFormula#%s" % self.text

#List of PatternItems which in order compose the grammar formula to apply
class PatternFormula(models.Model): 
    text = models.CharField(max_length=140) #pitem.name = "I-adjective + naru"
    entry = models.ManyToManyField(GrammarEntry) # After creating object,  use grammarpattern.add(<PatternFormula pointer>)

    def __str__(self):
        return "PatternFormula#%s" % self.text

class PatternItem(models.Model): #Can be POS or MODIFIER
    text = models.CharField(max_length=140) #pitem.text = "NARU particle, meaning to become"
    symbol = models.CharField(max_length=50) #pitem.symbol = "NARU" < in Japanese
    formula = models.ManyToManyField(PatternFormula) # After creating object,  use patternformula.add(<PatternItem pointer>)

    def __str__(self):
        return "PatternItem#%s" % str(self.pk)+" "+self.text

    
#TODO: -> Save and Load data from XML files.. TODO <-

#Class Vocabulary
#Defines single Vocabulary entry, following JLPT N5-N1 lists...
class Vocabulary(models.Model): 
    seqid = models.IntegerField(default=0) #This has to match the JDICT entry ?
    pub_date = models.DateTimeField('date published')
    jlpt = models.IntegerField(choices=JLPT_LEVELS, default=5)
    level = models.IntegerField(default=0) # Total of 1-1024

    text = models.CharField(max_length=140, default="") #Keb or Reb from Dictionary Entry  ( Kanji or combination of Kanji and Furigana )
    furigana = models.CharField(max_length=140, default="")
    romanji = models.CharField(max_length=140, default="")
    pos = models.IntegerField(choices=POS_ITEMS, default=TBD) #Part of Speech

    def __str__(self):
        return "Vocabulary:{0} : {1}".format((self.text), (self.furigana))

    def get_text(self):
        if self.text == "":
            return self.furigana
        else:
            return self.text

    def get_furigana(self):
        return self.furigana

    def get_romanji(self):
        return self.romanji

    def get_definition(self, num):
        definitions = self.langdefinition_set.all()
        if len(definitions) != 0 and len(definitions) > num:
            definition = definitions[num].entext
            return definition
        else : 
            definition = ""
            return definition 

#Class LangDefinition: 
#Placeholder for definitions of the entry, (a Vocabulary entry can have multiple different meanings)
class LangDefinition(models.Model):
    entry = models.ManyToManyField(Vocabulary) # After creating object,  use definition.add(<Vocabulary pointer>) #TODO: Make a base LangEntry Class?
    jptext = models.CharField(max_length=140, default="")  #Japanese definition entry
    entext = models.CharField(max_length=140, default="")  #English definition about entry

    def __str__(self):
        return "Definition#%s" % self.pk

#Class LangNote: 
#Notes about the specific entry, to be noted to users as a reminder, not to be tested.
class LangNote(models.Model):
    entry = models.ManyToManyField(Vocabulary) # After creating object,  use langnote.add(<Vocabulary pointer>)  #TODO: Make a base LangEntry Class?
    jptext = models.CharField(max_length=140, default="")  #Japanese note about entry
    entext = models.CharField(max_length=140, default="")  #English note about entry

    def __str__(self):
        return "Note#%s" % self.pk

#Class LangTag: 
#Tag about the specific entry, single word useful tag that can help categorize entries ( #slang, #honorific, #sports, etc.. ) #TODO: Can get from Dictionary
class LangTag(models.Model):
    entry = models.ManyToManyField(Vocabulary) # After creating object,  use langtag.add(<Vocabulary pointer>)  #TODO: Make a base LangEntry Class?
    jptext = models.CharField(max_length=140, default="")  #Japanese tag
    entext = models.CharField(max_length=140, default="")  #English tag

    def __str__(self):
        return "Tag#%s" % self.pk
#Class Verb
