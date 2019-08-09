from django.shortcuts import *
from django.http import HttpResponse
from django.template import RequestContext

from .models import *
from .forms import *
from .apps import *

# Create your views here.
def home(request):

    landing = generateLanding()

    return render(request, "home.html", {"landing" : landing})

def ideas(request):

    ideas = Idea.objects.all()

    if request.method == 'POST':
        submitIdea = IdeaForm(request.POST) # The submitted form

        if submitIdea.is_valid():
            # TODO: Add message success
            category = submitIdea.cleaned_data['category']
            content = submitIdea.cleaned_data['content']
            Idea.objects.create(category=category, content=content)
    
    form = IdeaForm()

    return render(request, "ideas.html", {'form' : form, 'ideas': ideas})

def removeIdea(request, idea):

    i = Idea.objects.get(id=idea).delete()
    return redirect('/dashboard/ideas')

def editIdea(request, idea):

    i = Idea.objects.get(id=idea)
    
    if request.method == 'POST':
        editIdea = IdeaForm(request.POST)

        if editIdea.is_valid():
            new_category = editIdea.cleaned_data.get("category")
            new_content = editIdea.cleaned_data.get("content")
           
            if len(new_category) > 0:
                i.category=new_category

            if len(new_content) > 0:
                i.content=new_content

            i.save()
    
    
    return redirect('/dashboard/ideas')

def todos(request):

    if Todo.objects:
        todos = Todo.objects.all()

    if request.method == 'POST':
        submitTodo = TodoForm(request.POST) # The submitted form

        if submitTodo.is_valid():
            # TODO: Add message success
            category = submitTodo.cleaned_data['category']
            content = submitTodo.cleaned_data['content']
            dateDue = submitTodo.cleaned_data['dateDue']
            
            Todo.objects.create(category=category, content=content, dateDue=dateDue, completed=False)
    
    form = TodoForm()

    return render(request, "todo.html", {'form' : form, 'todos': todos})

def removeTodo(request, todo):
    i = Todo.objects.get(id=todo).delete()
    return redirect('/dashboard/todos')

def toggleTodoCompleted(request, todo):
    t = Todo.objects.get(id=todo)
    t.completed = not(t.completed)
    t.save()
    return redirect('/dashboard/todos')

def editTodo(request, todo):

    t = Todo.objects.get(id=todo)

    if request.method == 'POST':
        editTodo = TodoForm(request.POST)

        if editTodo.is_valid():
            new_category = editTodo.cleaned_data.get("category")
            new_content = editTodo.cleaned_data.get("content")
            new_dateDue = editTodo.cleaned_data.get("dateDue")

            if len(new_category) > 0:
                t.category = new_category

            if len(new_content) > 0:
                t.content = new_content
            
            if new_dateDue:
                t.dateDue = new_dateDue

            t.save()

    return redirect('/dashboard/todos')

def calendar(request):
    
    return render(request, "calendar.html")