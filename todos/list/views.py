from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import TodoForm

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
  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
      formInstance = form.save(commit=False)
      formInstance.user = request.user
      formInstance.save()
      return HttpResponse('thanks')
  else:
    form = TodoForm()
    return render(request, 'list/new.html', {'form':form})