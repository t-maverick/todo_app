from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from .forms import TaskItemCreator
from .models import TaskItem

class HomePage(ListView):
    # model = TaskItem
    template_name = 'notes/home.html'
    
    def get_queryset(self):
        return reverse_lazy('home-page')

class TaskList(ListView):
    model = TaskItem

class TaskItem(ListView):
    model = TaskItem
    template_name = 'notes/note.html'
    
class CreateTask(CreateView):
    model = TaskItem
    template_name = 'notes/task_create_form.html'
    form_class = TaskItemCreator
    succes_url = reverse_lazy('tasks')
    
class UpdateTask(UpdateView):
    model = TaskItem
    
class DeleteTask(DeleteView):
    model = TaskItem
    