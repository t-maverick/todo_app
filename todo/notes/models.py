from sre_parse import CATEGORIES
from unittest.mock import DEFAULT
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    DEFAULT = 'DEFAULT'
    PERSONAL = 'PERSONAL'
    SHOPPING = 'SHOPPING'
    WISHLIST = 'WISHLIST'
    WORK = 'WORK'
    CATEGORIES = (
    (DEFAULT,DEFAULT),
    (PERSONAL,PERSONAL),
    (SHOPPING,SHOPPING),
    (WISHLIST,WISHLIST),
    (WORK,WORK)
    )
    def choice_or_make(category):
        if category != True:
            raise ValidationError(_('You should make some category'), params={'category': category})
    # you shold make it work in view, not in models
    # category(category_create, category_default)
    category = models.CharField(max_length=10, blank=True, validators=[choice_or_make])
    
    def __str__(self):
        return self.category
    
class TaskItem(models.Model):
    
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=timezone.now)
    unfinished = models.BooleanField(default=True)
    category_task = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title