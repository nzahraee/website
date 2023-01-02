from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    categoryw = Category.objects.all()
    return render(request,'home/home.html',{'categoryw':categoryw})

def all_product(request,id=None):
    products = product.objects.all()
    category = Category.objects.all()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(category=data)
    return render(request,'home/product.html',{'products':products})

def apt(request):
    return render(request, 'home/jabama.html')

def user_profile(request):
    profile = profile.objects.get(user_id=request.user.id)
    return render(request, 'home/profile.html',{'profile':profile})

def product_detail(request,id=None):
    productd = product.objects.get(id=id)
    return render(request,'home/detail.html',{'productd':productd})

def category(request):
    return render(request, 'home/category.html',{'category':category})