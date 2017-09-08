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
