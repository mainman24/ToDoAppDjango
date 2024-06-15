from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.


def index(request):
    tasks = Task.objects.all()

    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            # Refreshes the page
            return redirect('todoapps:index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todoapps/index.html', context)


def update_task(request, topic_id):
    task = Task.objects.get(id=topic_id)

    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('todoapps:index')

    context = {'form': form, 'task': task}
    return render(request, 'todoapps/updateTask.html', context)


def delete_task(request, topic_id):
    task = Task.objects.get(id=topic_id)

    if request.method == 'POST':
        task.delete()
        return redirect('todoapps:index')

    context = {'task': task}
    return render(request, 'todoapps/delete_task.html', context)


def complete_task(request, topic_id):
    task = Task.objects.get(id=topic_id)
    task.completed = True
    task.save()
    return redirect('todoapps:index')
