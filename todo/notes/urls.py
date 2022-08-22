from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('task-list/', views.TaskList.as_view(), name='tasks'),
    path('task/<str:pk>/', views.TaskDetail.as_view(), name='task'),
    path('update-task/<str:pk>/', views.UpdateTask.as_view(), name='update-task'),
    path('create-task/', views.CreateTask.as_view(), name='create-task'),


]
