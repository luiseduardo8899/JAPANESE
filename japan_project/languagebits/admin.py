from django.contrib import admin
from languagebits.models import *

# Register your models here.
admin.site.register(Kana)
admin.site.register(Vocabulary)
admin.site.register(LangDefinition)
admin.site.register(GrammarEntry)
admin.site.register(GrammarDescription)
admin.site.register(PatternFormula)
admin.site.register(PatternItem)
admin.site.register(KanjiEntry)
admin.site.register(KanjiDescription)
admin.site.register(Onyomi)
admin.site.register(Kunyomi)
