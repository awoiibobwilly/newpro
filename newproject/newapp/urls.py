from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexpage'),
    path('index', views.create_task, name='create_task'),
    path('<day>', views.taskall, name='taskall'),
    
    
    
]