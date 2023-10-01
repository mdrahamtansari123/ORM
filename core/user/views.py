from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def home(request):
    for p in Student.objects.all().select_realeted('name')[0:5]:
        print(p.name)
        print(p.name.age)
    return 
