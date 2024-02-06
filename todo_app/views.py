from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'todos': todos, 'form': form}
    return render(request, 'todo_app/home.html', context)

def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect('home')

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')
