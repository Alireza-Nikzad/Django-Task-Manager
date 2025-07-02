from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description= description)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'firstapp/home.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id= task_id)
    task.delete()
    return redirect('/')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed= True
    task.save()
    return redirect('/')

def uncomplete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = False
    task.save()
    return redirect('/')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get("description")
        task.save()
        return redirect('/')
    
    return render(request, 'firstapp/edit.html', {'task': task})