from django.urls import path
from . import views


app_name='home'
urlpatterns= [
    path('',views.home,name='home'),
    path('product/',views.all_product,name='product'),
    path('apt/',views.apt,name='apt'),
    path('profile/', views.user_profile,name='profile'),
    path('products/', views.all_product,name='products'),
    path('detail/<int:id>/', views.product_detail, name='detail'),
    path('category/<int:id>/', views.all_product, name='category'),
]