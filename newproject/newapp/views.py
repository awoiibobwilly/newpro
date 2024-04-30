from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tasks = {'Monday': 'Go Shopping','Tuesday': 'Gym Time','Wednesday': 'Office Work','Thursday': 'Business Meeting','Friday': 'Recreation Time'}


def taskall(request,day):
    todo = tasks[day]
    return render(request, 'newapp/base.html', {'bob2': todo, 'title': day})

def index(request):
    return HttpResponse('<h1>TO DO LIST</h1>')

