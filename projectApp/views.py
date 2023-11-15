from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, 'projectApp/main.html')

def login(request):
   return render(request, 'projectApp/login.html')
def signup(request):
   return render(request, 'projectApp/signup.html')

def product(request):
   return render(request, 'projectApp/product.html')

def products(request):
   return render(request, 'projectApp/products.html')
def add(request):
   return render(request, 'projectApp/add.html')
def update(request):
   return render(request, 'projectApp/update.html')