from django.db import models
from django import forms

# Create your models here.

class Idea(models.Model):

    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateEdited = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=32)
    content = models.TextField()

class Todo(models.Model):

    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateDue = models.DateField(auto_now=False, auto_now_add=False)
    category = models.CharField(max_length=32)
    content = models.TextField()
    completed = models.BooleanField()



