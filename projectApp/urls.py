from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup, name='signup'),
    path('items/products',views.products, name='products'),
    path('item/product/<int:product_id>',views.product , name='product'),
    path('item/product/add',views.add , name='add'),
    path('item/product/update',views.update , name='update'),
]