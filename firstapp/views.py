from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Create task linked to current user
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('home')  # or redirect('/')
    # Show only tasks for logged-in user
    tasks = Task.objects.filter(user=request.user)
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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'firstapp/signup.html', {'form': form})

    