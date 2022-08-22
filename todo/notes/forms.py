from django import forms
from .models import TaskItem

class TaskItemForm(forms.ModelForm):
    
    class Meta:
        model = TaskItem
        fields = ("username", "title", "text", "due_date",)
