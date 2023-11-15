from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request, 'projectApp/main.html')

def login(request):
   return render(request, 'projectApp/login.html')

def displayAll(request):
   return render(request, 'projectApp/dispalyAll.html')

def display(request):
   return render(request, 'projectApp/display.html')
def add(request):
   return render(request, 'projectApp/add.html')
def update(request):
   return render(request, 'projectApp/update.html')