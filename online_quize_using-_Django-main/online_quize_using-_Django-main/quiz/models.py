from tkinter.messagebox import QUESTION
from django.db import models

# Create your models here.
class Exam (models.Model):
    QUESTION = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    corrans = models.CharField(max_length=200)
