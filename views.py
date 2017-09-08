from django.shortcuts import render
from django.http import HttpResponse
from .models import myapp
# Create your views here.

def index(request):
    myappdata = myapp.objects.all()
    context = {
        'listdata': myappdata
    }
    return render(request, 'index.html', context )

def details(request, todo_id):
    todo = myapp.object.get(id = todo_id)
    context = {
        'data': todo
    }
    return render(request, 'details.html', context)

