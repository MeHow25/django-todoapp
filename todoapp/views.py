from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('todo_list')
    
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todoapp/todo_list.html', context)

def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    
    status = "completed" if todo.completed else "marked as incomplete"
    messages.success(request, f'Task "{todo.title}" {status}!')
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.success(request, f'Task "{todo.title}" deleted successfully!')
    return redirect('todo_list')

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, 'todoapp/edit_todo.html', context)