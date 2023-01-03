from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from .models import *

def jabama(request,id=None):
    category = acomodation.objects.all()
    if id:
        data = acomodation.objects.get(id=id)
        category = acomodation.objects.get(name=data)
    return render(request,'jabama/home.html',{'category':category})

