from django.contrib import admin
from notes.models import NotesList, Note

admin.site.register(NotesList)
admin.site.register(Note)