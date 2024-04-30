from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tasks = {'Monday': 'Go Shopping','Tuesday': 'Gym Time','Wednsday': 'Office Work','Thursday': 'Business Meeting','Friday': 'Recreation Time'}


def taskall(request,day):
    todo = tasks[day]
    return HttpResponse(todo)

def index(request):
    return HttpResponse('<h1>TO DO LIST</h1>')

