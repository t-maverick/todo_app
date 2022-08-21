from socket import fromshare
from django import forms
from .models import TaskItem

class TaskItemForm(forms.ModelForm):
    
    class Meta:
        model = TaskItem
        fields = ("title", "text", "due_date", "category")
