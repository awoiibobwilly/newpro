from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TaskForm
from .models import Task # we are importing the model
from django.urls import reverse

# Create your views here.
tasks = {'Monday': 'Go Shopping','Tuesday': 'Gym Time','Wednesday': 'Office Work','Thursday': 'Business Meeting','Friday': 'Recreation Time'}


def taskall(request):
    # todo = tasks.get(day)
    form = TaskForm()   #this is creating an instance (instanciation), we have invoked the class.
    return render(request, 'newapp/base.html', {'bob2': todo, 'title': day, 'form': form})

def index(request):
    return HttpResponse('<h1>TO DO LIST</h1>')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # print('create')
            a_name = form.cleaned_data ['name']    #these field names are from the model, name as it is in the left can change or vary, but what us is in [] should be maintained
            b_details = form.cleaned_data ['details'] #these field names are from the 
            c_number_of_people = form.cleaned_data ['number_of_people'] 
            d_date = form.cleaned_data ['date'] #these field names 
            e_day_of_week = form.cleaned_data ['day_of_week'] #these field names 
            Task.objects.create(name=a_name, details = b_details, number_of_people=c_number_of_people, date=d_date, day_of_week=e_day_of_week)#We pass the actual data as it is in the model
            return HttpResponseRedirect(reverse('indexpage'))
            return redirect('/index')      
    else:
        # tasklist = []
        form = TaskForm()
    tasklist = Task.objects.all() #We are retrieving list and sending it back
    return render(request, 'newapp/base.html', {'form': form, 'tasklist': tasklist})

# def __str__(self):
#     return self.task_name

def delete_tasks(request, task_id):
    Task.objects.filter(id=task_id).delete()
    redirect_url = reverse('create_task')
    return HttpResponseRedirect(redirect_url)


def edit_tasks(request, task_id):
    task= Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            a_name = form.cleaned_data ['name']    
            b_details = form.cleaned_data ['details'] 
            c_number_of_people = form.cleaned_data ['number_of_people'] 
            d_date = form.cleaned_data ['date']
            e_day_of_week = form.cleaned_data ['day_of_week'] 
            
            #Updating fields in the database 

            task.name = a_name
            task.details = b_details
            task.number_of_people = c_number_of_people
            task.date = d_date
            task.day_of_week = e_day_of_week
            task.save()
            redirect_url = reverse('create_task')
            return HttpResponseRedirect(redirect_url)
    else:
        form = TaskForm(initial={'name': task.name, 'details': task.details, 'number_of_people': task.number_of_people, 'date': task.date, 'day_of_week': task.day_of_week})
        return render(request, 'newapp/edit_task.html', {'form': form, 'task_id': task_id})

        
                
    
    

