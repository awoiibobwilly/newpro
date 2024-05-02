from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TaskForm
from .models import Task # we are import the model
from django.urls import reverse

# Create your views here.
tasks = {'Monday': 'Go Shopping','Tuesday': 'Gym Time','Wednesday': 'Office Work','Thursday': 'Business Meeting','Friday': 'Recreation Time'}


def taskall(request,day):
    todo = tasks.get(day)
    form = TaskForm()   #this is creating an instance (instanciation), we have invoked the class.
    return render(request, 'newapp/base.html', {'bob2': todo, 'title': day, 'form': form})

def index(request):
    return HttpResponse('<h1>TO DO LIST</h1>')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            a_name = form.cleaned_data ['name']    #these field names are from the model, name as it is in the left can change or vary, but what us is in [] should be maintained
            b_details = form.cleaned_data ['details'] #these field names are from the 
            awoii_number_of_people = form.cleaned_data ['number_of_people'] 
            c_date = form.cleaned_data ['date'] #these field names 
            d_day_of_week = form.cleaned_data ['day_of_week'] #these field names 
            Task.objects.create(name=task_name, details = bob_details, number_of_people=awoii_number_of_people, date=dwe_date, day_of_week=nino_day_of_week)#We pass the actual data as it is in the model
            # return HttpResponseRedirect(reverse('indexpage'))
    else:
        form = TaskForm()
        tasklist = Task.objects.all() #We are retrieving list and sending it back
    return render(request, 'newapp/base.html', {'form': form})

# def __str__(self):
#     return self.task_name
        
                
    
    
    # form = TaskForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    # return render(request, 'newapp/create_task.html', {'form': form})

