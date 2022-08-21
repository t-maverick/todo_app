from socket import fromshare
from django import forms
from .models import TaskItem

class TaskItemCreator(forms.ModelForm):
    
    class Meta:
        model = TaskItem
        forms = ('title', 'text', 'due_date', 'category')