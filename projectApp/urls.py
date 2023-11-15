from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('signup/',views.signup),
    path('items/products/services',views.products),
    path('item/product/service',views.product),
    path('item/product/add',views.add),
    path('item/product/update',views.update),

]