from django.contrib import admin
from languagebits.models import Kana, Vocabulary, GrammarEntry, GrammarDescription, PatternFormula, PatternItem

# Register your models here.
admin.site.register(Kana)
admin.site.register(Vocabulary)
admin.site.register(GrammarEntry)
admin.site.register(GrammarDescription)
admin.site.register(PatternFormula)
admin.site.register(PatternItem)
