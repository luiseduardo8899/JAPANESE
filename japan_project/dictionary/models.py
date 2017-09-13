from django.db import models
from django.utils import timezone
import datetime


#SenseTag Ids:
POS_TAG 		= 0 #Part of Speech
MISC_TAG 		= 1 #Miscellaneous Tag
FIELD_TAG 		= 2 #Field of study/work tag
DIALECT_TAG 	= 3 #Dialect source tag ( Kyoto ben, Kansai ben, etc.. ) 
#If need to add more tag types to SenseTag continue here.. #5

#START REBTAG_IDS
GIKUN_TAG = 0
IK_TAG = 1
OIK_TAG = 2
OK_TAG = 3

REBTAG_IDS = (
    (GIKUN_TAG , "gikun_tag"  ), #gikun (meaning as reading) or jukujikun (special Kanji reading)
    (IK_TAG , "ik_tag"  ), # irregular Kanji usage
    (OIK_TAG , "oik_tag"  ), #old or irregular kana form
    (OK_TAG , "ok_tag" ) # word containing outdated Kanji
)

SENSETAG_IDS=(
    #TODO: include all missing tags
    (POS_TAG , "POS_TAG"), #Part of Speech
    (MISC_TAG, "MISC_TAG"),  #Miscellaneous Tag
    (FIELD_TAG, "FIELD_TAG"), #Field of study/work tag
    (DIALECT_TAG, "DIALECT_TAG"), #Dialect source tag ( Kyoto ben, Kansai ben, etc.. ) 
)


#TODO: Tags which come with JDICT and may be useful moving forward:
#1. Reading element <re_nokanji> : katana readings which may are used standalone
#2. Reading element <re_restr> : This element is used to indicate when the reading only applies to a subset of the keb elements in the entry.
#3. Reading element: <re_inf> : General coded information pertaining to the specific reading.  Typically it will be used to indicate some unusual aspect of the reading
#4 <!ELEMENT stagk (#PCDATA)> --> model
#5 <!ELEMENT stagr (#PCDATA)> --> model
#  4,5:  <!-- These elements, if present, indicate that the sense is restricted to the lexeme represented by the keb and/or reb. -->



#Class Entry 
#Class for all dictionary entries (nouns, verbs, adjectives, etc)
class Entry(models.Model):
    level = models.IntegerField(default=0)     #level of difficulty (0-4095)
    #jlpt_level = models.IntegerField(choices=JLPT_LEVELS, default=JLPT_N5)#level of difficulty (1-5) : N1 - N5 (level other than 1-5 will mean not currently classified) #TODO: add this is noun, verb, etc.. class
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Entry#%s" % self.pk

    #placeholder for checking how long ago the entry was made ( detect novel words )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=30)

    class Meta:
        ordering = ['pub_date']

#Class Keb: 
#Different ways an entry can be written (i.e different kanjis)
#A Keb object may match multiple Entry objects
class Keb(models.Model):
    entry = models.ManyToManyField(Entry) # After creating object,  use keb.add(<Entry pointer>)
    text = models.CharField(max_length=200)  #Dictionary entry text in Japanese

    def __str__(self):
        return self.text


#Class Reb: 
#Different ways an entry could be pronounced
#A Reb object may match multiple Entry objects ( same reading different meaning )
class Reb(models.Model):
    entry = models.ManyToManyField(Entry) # After creating object,  use reb.add(<Entry pointer>)
    furigana = models.CharField(max_length=100)  #Spelling in Furigana 
    romanji = models.CharField(max_length=100)  #Spelling in Romanji

    def __str__(self):
        return self.furigana

#Class Sense: 
#Placeholder for definitions of the entry, contains the gloss and tags (a word can have multiple different meanings)
class Sense(models.Model):
    entry = models.ManyToManyField(Entry) # After creating object,  use sense.add(<Entry pointer>)

    def __str__(self):
        return "Sense#%s" % self.pk

class SenseTag(models.Model):
    sense = models.ManyToManyField(Sense) # After creating object,  use sensetag.add(<Sense pointer>)
    text = models.CharField(max_length=200)  #English tag added to the entry
    tid = models.IntegerField(choices=SENSETAG_IDS, default=1)

    def __str__(self):
        if self.tid == POS_TAG : #Part of Speech
            return "SenseTag: POS: %s" % self.text
        if self.tid == MISC_TAG : #Miscellaneous Tag
            return "SenseTag: MISC: %s" % self.text
        if self.tid == FIELD_TAG : #Field of study/work tag
            return "SenseTag: FIELD: %s" % self.text
        if self.tid == DIALECT_TAG : #Dialect source tag ( Kyoto ben, Kansai ben, etc.. ) 
            return "SenseTag: DIALECT: %s" % self.text

#Aditional information about a specific entry, comes in the form of pure text
class SenseInf(models.Model):
    sense = models.ManyToManyField(Sense) # After creating object,  use sensetag.add(<Sense pointer>)
    text = models.CharField(max_length=250)  #English description about the entry

    def __str__(self):
            return "SenseInf: %s" % self.text

#Class Re_Inf: 
#General coded information pertaining to the specific reading.
#Typically it will be used to indicate some unusual aspect of the reading
class RebTag(models.Model):
    entry = models.ManyToManyField(Reb) # After creating object,  use re_inf.add(<Reb pointer>)
    text = models.CharField(max_length=200)  #English definition of the entry
    tid = models.IntegerField(choices=REBTAG_IDS, default=1)

class Gloss(models.Model):
    sense = models.ManyToManyField(Sense) # After creating object,  use gloss.add(<Sense pointer>)
    text = models.CharField(max_length=200)  #English definition of the entry
    def __str__(self):
            return "Gloss: %s" % self.text

#Class: Antonym
class Antonym(models.Model):
    sense = models.ManyToManyField(Sense) # After creating object,  use sense.add(<Entry pointer>)
    text = models.CharField(max_length=200)  #Japanese text entry of the antonym

    def __str__(self):
            return "Antonym: %s" % self.text

#Class: Synonym
class Synonym(models.Model):
    sense = models.ManyToManyField(Sense) # After creating object,  use sense.add(<Entry pointer>)
    text = models.CharField(max_length=200)  #English definition of the entry

    def __str__(self):
            return "Synonym: %s" % self.text

#Class: LSource 
class LSource(models.Model): 
    sense = models.ManyToManyField(Sense) # After creating object,  use sdialect.add(<Sense pointer>)
    lang = models.CharField(max_length=10, default="en")  #Language Source of the entry ( defaults to english )
    text = models.CharField(max_length=200, default="")  #English definition of the entry
    ls_wasei  = models.BooleanField(default=False) #If True: Meaning not corresponding to a real word in the source lang.
    full = models.BooleanField(default=True) # Meaning the term comes from a full vocabulary word in the source language
                                            #if False, it means the word is composed from parts of words which 
                                            #may not correspond to an actual term in the source language.
    def __str__(self):
            return "LSource: %s" % self.text

