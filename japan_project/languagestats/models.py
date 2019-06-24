from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from languagebits.models import Vocabulary
import math

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

#Types of Memory 
SHORT_TERM = 0
MID_TERM = 1
LONG_TERM = 2
NEW_TERM = 3
NEW_ITEM_LIMIT = 15 #15 new items per login

MEMORY_TYPES = {
    (NEW_TERM, "NEW_TERM"),
    (SHORT_TERM, "SHORT_TERM"),
    (MID_TERM, "MID_TERM"),
    (LONG_TERM, "LONG_TERM"),
}

#Memory :
class Memory(models.Model):
    user = models.ForeignKey(User) 
    mem_type = models.IntegerField(choices=MEMORY_TYPES, default=SHORT_TERM)

    def __str__(self):
        if self.mem_type == NEW_TERM :
            s = "NEW_TERM"
        elif self.mem_type == SHORT_TERM :
            s = "SHORT_TERM"
        elif self.mem_type == MID_TERM :
            s = "MID_TERM"
        elif self.mem_type == LONG_TERM :
            s = "LONG_TERM"
        return "Memory:[%s] : %s" % (self.mem_type , s)

#LongTermMemoty > Items already learned ( quized out )


#TODO: def load_item(memory, item):
#TODO:     #check if item already in that memory
#TODO:     if 
#TODO:     else:
#TODO:         item.memory.add(memory)
#TODO: def remove_item(memory, item):
#TODO: def get_rand_item(memory, item):


#VocabStat:  Clones VocabularyEntry, and is submitted to user memory
class VocabStats(models.Model):
    entry = models.ForeignKey(Vocabulary) # After creating object,  use definition.add(<Vocabulary pointer>) #TODO: Make a base LangEntry Class?
    user = models.ForeignKey(User,  blank=True, null=True) # After creating object,  use definition.add(<Vocabulary pointer>) #TODO: Make a base LangEntry Class?
    memory = models.ManyToManyField(Memory, blank=True, null=True) #memory where this entry is located
    seqid = models.IntegerField(default=0) #Matches VocabId
    jlpt = models.IntegerField(choices=JLPT_LEVELS, default=5)
    level = models.IntegerField(default=0) # Total of 1-1024
    text = models.CharField(max_length=140, default="") #Keb or Reb from Dictionary Entry  ( Kanji or combination of Kanji and Furigana )
    furigana = models.CharField(max_length=140, default="")

    add_date = models.DateTimeField('date published') #Date added to users memory
    last_read_date = models.DateTimeField('date published') #Date the vocab was last read
    last_quiz_date = models.DateTimeField('date published') #Date the vocab was last quized
    times_read = models.IntegerField(default=0) #number of times it was presented in a flashcard
    times_quized = models.IntegerField(default=0)
    furigana_score  = models.IntegerField(default=0) #1-100
    pronunciation_score  = models.IntegerField(default=0) #1-100
    definition_score  = models.IntegerField(default=0) #1-100

    def __str__(self):
        return "VocabStat:{0} : {1}".format((self.text), (self.furigana))

    def get_text(self):
        if self.text == "":
            return self.furigana
        else:
            return self.text

    def get_furigana(self):
        return self.furigana

    def get_entry(self):
        return self.entry

    def quiz_def_correct(self):
        temp = (self.definition_score*self.times_quized)+100
        score_temp =  math.ceil(temp /(self.times_quized+1))
        self.times_quized = self.times_quized + 1
        self.definition_score = score_temp 
        self.save()

    def quiz_def_incorrect(self):
        temp = self.definition_score*self.times_quized+0
        score_temp =  math.floor(temp /(self.times_quized+1))
        self.times_quized = self.times_quized + 1
        self.definition_score = score_temp
        self.save()

    def quiz_fur_correct(self):
        temp = (self.furigana_score*self.times_quized)+100
        score_temp =  math.ceil(temp /(self.times_quized+1))
        self.times_quized = self.times_quized + 1
        self.furigana_score = score_temp 
        self.save()

    def quiz_fur_incorrect(self):
        temp = self.furigana_score*self.times_quized+0
        score_temp =  math.floor(temp /(self.times_quized+1))
        self.times_quized = self.times_quized + 1
        self.furigana_score = score_temp
        self.save()

    #TODO: get definition from here: def get_definition(self, num):
    #TODO: get definition from here:     definitions = self.langdefinition_set.all()
    #TODO: get definition from here:     if len(definitions) != 0 and len(definitions) > num:
    #TODO: get definition from here:         definition = definitions[num].entext
    #TODO: get definition from here:         return definition
    #TODO: get definition from here:     else : 
    #TODO: get definition from here:         definition = ""
    #TODO: get definition from here:         return definition 
