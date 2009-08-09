from django.contrib import admin
from prana.models import Word, Verb

class WordAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "date")

admin.site.register(Word, WordAdmin)

class VerbAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "date")

admin.site.register(Verb, VerbAdmin)
