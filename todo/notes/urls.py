from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('notes/', views.NotesList.as_view(), name='notes-list'),

]
