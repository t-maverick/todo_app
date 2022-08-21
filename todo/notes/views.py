from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import TaskItem

class HomePage(ListView):
    # model = TaskItem
    template_name = 'notes/home.html'
    
    def get_queryset(self):
        return reverse_lazy('home-page')