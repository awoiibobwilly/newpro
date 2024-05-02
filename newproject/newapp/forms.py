from django import forms 

class TaskForm(forms.Form):
    name = forms.CharField(max_length=200)
    details = forms.CharField(max_length=1000)
    number_of_people = forms.IntegerField()
    date = forms.DateField()
    day_of_week = forms.CharField(max_length=20)
    
    
