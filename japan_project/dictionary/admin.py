from django.contrib import admin
from dictionary.models import Entry, Sense, Gloss, Reb, Keb, LSource, SenseInf, SenseTag

#Registered models go here:
admin.site.register(Entry)
admin.site.register(Keb)
admin.site.register(Reb)
admin.site.register(Sense)
admin.site.register(Gloss)
admin.site.register(SenseTag)
admin.site.register(SenseInf)
admin.site.register(LSource)
