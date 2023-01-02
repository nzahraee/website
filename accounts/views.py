from django.shortcuts import render, redirect
from . forms import userRegisterForm
from django.contrib.auth.models import User

def user_register(request):
    if request.method =='Post':
        form = userRegisterForm (request.Post)
        if form.is_valid():
            data = form.cleaned_data
            user.object.create_user(user_name=data['user_name'], email=data['email'],first_name=data['first_name'],
                                    last_name = data['last_name'], password=data['password_2'])
        return redirect('home:home')
    else:
        form =  userRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html',context)

