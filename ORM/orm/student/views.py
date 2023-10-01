from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q
# Create your views here.

def student_list(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    # print(connection.queries)

    return render(request, 'index.html',{'posts':posts})
def student(request):

    # posts = Student.objects.filter(surname__startswith= 'rahat') | Student.objects.filter(surname__startswith= 'Alam')
    posts = Student.objects.filter() | Student.objects.filter()

    print(posts)
    print(posts.query)
    # print(connection.queries)

    return render(request, 'index.html',{'posts':posts})