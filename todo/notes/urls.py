from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListNotesList.as_view(), name='notes-list'),
]
