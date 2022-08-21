from unicodedata import category
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class User(models.Model):
    pass

class Category(models.Model):
    # you shold make it work in view, not in models
    # category(category_create, category_default)
    def choice_or_make(category):
        if len(category) <= 2: 
            raise ValidationError(
                (f'{category} category is too small, make it bigger'), params={'category': category},
            )
    category = models.CharField(max_length=10, null=True, blank=True, validators=[choice_or_make])
    
    def __str__(self):
        return self.category
    
class TaskItem(models.Model):
    
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=timezone.now)
    unfinished = models.BooleanField(default=True)
    category_task = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-unfinished']