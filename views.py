from django.shortcuts import render
from .models import myapp
# Create your views here.

def index(request):
    myappdata = myapp.objects.all()
    context = {
        'listdata': myappdata
    }
    return render(request, 'index.html', context )

def details(request, todo_id):
    todo = myapp.objects.get(id = todo_id)
    context = {
        'data': todo
    }
    return render(request, 'details.html', context)

def expression(request):
    return render(request, 'expression.html')

