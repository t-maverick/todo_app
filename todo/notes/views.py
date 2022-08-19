from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Note, NotesList

class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    fields ='__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'notes/register'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    
class HomePage(TemplateView):
    template_name = 'notes/home.html'
    
class NotesList(ListView):
    model = NotesList
    template_name = 'notes/notes-list.html'

class Note(ListView):
    model = Note
    template_name = 'notes/note.html'
    
    def get_queryset(self):
        return NotesList.objects.filter(notes_title_id = self.kwargs['list_id'])
    