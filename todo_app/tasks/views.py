from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tasks

def index(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')  # Get task ID if editing
        title = request.POST.get('task_title')
        is_completed = request.POST.get('is_completed') == 'true'  # Convert checkbox to boolean

        if task_id:  # Editing an existing task
            task = get_object_or_404(Tasks, id=task_id)
            task.title = title
            task.is_completed = is_completed
            task.save()
            messages.success(request, f'Task "{task.title}" updated successfully.')
        else:  # Creating a new task
            if title:
                task = Tasks(title=title, is_completed=is_completed)
                task.save()
                messages.success(request, f'Task "{title}" has been added successfully.')
            else:
                messages.warning(request, 'Task title cannot be empty.')

        return redirect('index')  # Redirect after POST to avoid re-submission

    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, f'Task "{task.title}" deleted successfully.')

    return redirect('index')
