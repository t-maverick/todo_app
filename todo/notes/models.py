from wsgiref.validate import validator
from django.db import models
from django.urls import reverse

class NotesList(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def get_absolute_url(self):
        return reverse("notes-list", args=[self.id])
    
    def __str__(self):
        return self.title
    
class Note(models.Model):
    note_title = models.CharField(max_length=20, null=True, blank=True)
    note_text = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_edited = models.DateTimeField(auto_now_add=True, blank=True)
    note_list = models.ForeignKey(NotesList, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.note_list.id), str(self.id)])
    
    def __str__(self):
        return f'{self.note_text} due: {self.date_created}'
    
    class Meta:
        ordering = ['date_created']