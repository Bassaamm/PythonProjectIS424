from django import forms
from .models import  Product
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']