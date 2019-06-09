from django.db import models


#Types of Memory 
SHORT_TERM = 0
LONG_TERM = 1

MEMORY_TYPES = {
    {SHORT_TERM, "SHORT_TERM"),
    {LONG_TERM, "LONG_TERM"),
}

#Memory :
class Memory(models.Model):
    user = models.ForeignKey(User) 
    mem_type = models.IntegerField(choices=MEMORY_TYPES, default=SHORT_TERM)

#LongTermMemoty > Items already learned ( quized out )

#VocabStat:  Clones VocabularyEntry, and is submitted to user memory
class VocabStats(models.Model):
    entry = models.ForeignKey(Vocabulary) # After creating object,  use definition.add(<Vocabulary pointer>) #TODO: Make a base LangEntry Class?
    user = models.ForeignKey(User) # After creating object,  use definition.add(<Vocabulary pointer>) #TODO: Make a base LangEntry Class?
    memory = models.ManytoManyField(Memory) #memory where thsi entry is located
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

    #TODO: get definition from here: def get_definition(self, num):
    #TODO: get definition from here:     definitions = self.langdefinition_set.all()
    #TODO: get definition from here:     if len(definitions) != 0 and len(definitions) > num:
    #TODO: get definition from here:         definition = definitions[num].entext
    #TODO: get definition from here:         return definition
    #TODO: get definition from here:     else : 
    #TODO: get definition from here:         definition = ""
    #TODO: get definition from here:         return definition 
