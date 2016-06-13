from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Todo

def index(request):
  todo_list = Todo.objects.order_by('-created_at')[:5]
  context = {"todo_list": todo_list}
  return render(request, "list/index.html", context)


def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo':todo}
    return render(request, 'list/detail.html', context)

def new(request):
  return render(request, 'list/new.html')
