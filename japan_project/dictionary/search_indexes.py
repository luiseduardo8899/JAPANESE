import datetime
from haystack import indexes
from dictionary.models import Keb, Reb, Gloss, Entry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

#TODO: How to denormalize the Reb / Keb / Gloss related objects here

    #This defines how the Entry displays in search results..
    def get_model(self):
        return Entry

#TODO:    def index_queryset(self, using=None):
#TODO:        """Used when the entire index for model is updated."""
#TODO:        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

##REMOVE?## class KebIndex(indexes.SearchIndex, indexes.Indexable):
##REMOVE?##     text = indexes.CharField(document=True, use_template=True)
##REMOVE?## 
##REMOVE?##     def get_model(self):
##REMOVE?##         return Keb
##REMOVE?## 
##REMOVE?## #NO PUB DATE FOR THESE    def index_queryset(self, using=None):
##REMOVE?## #NO PUB DATE FOR THESE        """Used when the entire index for model is updated."""
##REMOVE?## #NO PUB DATE FOR THESE        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
##REMOVE?## 
##REMOVE?## class RebIndex(indexes.SearchIndex, indexes.Indexable):
##REMOVE?##     text = indexes.CharField(document=True, use_template=True)
##REMOVE?## 
##REMOVE?##     def get_model(self):
##REMOVE?##         return Reb
##REMOVE?## 
##REMOVE?## class GlossIndex(indexes.SearchIndex, indexes.Indexable):
##REMOVE?##     text = indexes.CharField(document=True, use_template=True)
##REMOVE?## 
##REMOVE?##     def get_model(self):
##REMOVE?##         return Gloss
