from django.db import models

# Create your models here.

#Name of task, Details of task, Number of people to work
class Task(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    number_of_people = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    day_of_week = models.CharField(max_length=20)
