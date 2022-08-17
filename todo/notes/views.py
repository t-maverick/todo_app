from msilib.schema import ListView
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView

from .models import Note, NotesList

class ListNotesList(ListView):
    model = NotesList
    template_name = 'notes/notes-list.html'

class ListNote(ListView):
    model = Note
    template_name = 'notes/note.html'
    
    def get_queryset(self):
        return NotesList.objects.filter(notes_title_id = self.kwargs['list_id'])
    