from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from .forms import TaskItemForm
from .models import TaskItem

class HomePage(ListView):
    # model = TaskItem
    template_name = 'notes/home.html'
    
    def get_queryset(self):
        return reverse_lazy('home-page')

class TaskList(ListView):
    model = TaskItem
    template_name = 'notes/task_list.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = TaskItem
    template_name = 'notes/task.html'
    context_object_name = 'task'

    
class CreateTask(CreateView):
    model = TaskItem
    template_name = 'notes/create_task.html'
    context_object_name = 'create_task'
    form_class = TaskItemForm
    succes_url = reverse_lazy('tasks')
    
class UpdateTask(UpdateView):
    model = TaskItem
    template_name = 'notes/update_task.html'
    context_object_name = 'update_task'
    form_class = TaskItemForm
    succes_url = reverse_lazy('tasks')
    
class DeleteTask(DeleteView):
    model = TaskItem
    