from django.shortcuts import redirect, render
from .forms import RegisterForm, AddProductForm, UpdateProductForm
from .models import Product as prodcutModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm
def index(request):
   return render(request, 'projectApp/main.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('items')
    else:
        form = AuthenticationForm()
    return render(request, 'projectApp/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('projectApp/items')
    else:
        form = RegisterForm()
    return render(request, 'projectApp/signup.html', {'form': form})

def products(request):
   products = prodcutModel.objects.all()
   return render(request, 'projectApp/products.html',{'products': products})

def product(request , product_id):
   product = prodcutModel.objects.get(id=product_id)
   context = {'product': product}
   return render(request, 'projectApp/product.html',context)

def add(request):
   if request.method == 'POST':
      addForm = AddProductForm(request.POST)
      addForm.save()
      redirect('item/product/add')
   else:
       addForm =  AddProductForm()
   return render(request, 'projectApp/add.html' , {'form': addForm})

def update(request):
    product = prodcutModel.objects.all()
    if request.method == 'POST':
        product = prodcutModel.objects.get(id=request.POST['select'])
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('update')
    return render(request, 'projectApp/update.html', {'products': product})