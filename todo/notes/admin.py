from django.contrib import admin
from notes.models import TaskItem, Category

admin.site.register(TaskItem)
admin.site.register(Category)