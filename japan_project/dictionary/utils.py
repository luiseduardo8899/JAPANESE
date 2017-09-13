from dictionary.models import Entry, Keb, Reb, Sense, Gloss
from random import *
from django.http import HttpResponseRedirect, HttpResponse

#Function: get_noun(word_id)
#Get a specififc entry based on an id (pk=word_id)
def get_entry_by_id(entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404("Gomenazai~~~ Entry  does not exist") #TODO: Retry, or fail back to retrieve different word ? 
    return entry

#Function: get_random_entry()
#Get a random entry from dictionary
def get_random_entry():
    entry = None

    #loop until we get a valid entry
    while ( entry == None ) :
        entry_id = randint(5, 5000)
        try:
            entry = Entry.objects.get(pk=entry_id)
        except Entry.DoesNotExist:
            entry == None
        
    return entry
