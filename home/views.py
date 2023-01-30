from django.shortcuts import render,redirect
from .models import *


def home(request):
    categoryw = Category.objects.filter(sub_cat=False)
    return render(request,'home/home.html',{'categoryw':categoryw})

def all_product(request,id=None):
    products = product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    # category = Category.objects.all()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(category=data)
    return render(request,'home/product.html',{'products':products,'category':category})

def apt(request):
    return render(request, 'home/jabama.html')

def user_profile(request):
    profile = profile.objects.get(user_id=request.user.id)
    return render(request, 'home/profile.html',{'profile':profile})

def product_detail(request,id=None):
    productd = product.objects.get(id=id)
    if product.status != 'None':
        if request.method == 'POST':
            variant = variants.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = variants.objects.get(id=var_id)
        else:
            variant = variants.objects.filter(product_variant_id=id)
            variants = v.objects.get(id=variant[0].id)
        context = {'product':product,'variant':variant,'variants':variants}
        return render(request, 'home/detail.html', context)
    else:
        return render(request,'home/detail.html',{'productd':productd})

def category(request):
    category2 = Category.objects.all()
    return render(request,'home/category.html',{'category2':category2})