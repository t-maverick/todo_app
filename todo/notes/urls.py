from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('task-list/', views.TaskList.as_view(), name='tasks')

]
