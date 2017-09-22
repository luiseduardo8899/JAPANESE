import datetime
from haystack import indexes
from dictionary.models import Keb, Reb, Gloss, Entry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    #This defines how the Entry displays in search results..
    def get_model(self):
        return Entry
