from django import forms
from django.contrib.auth.models import User


class userRegisterForm(forms.Form):
    user_name =  forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)

    def cleaned_data(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.validationError('user Exist')
        return User
    def cleaned_data(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise form.validationError('email duplicate')
        return email

    def cleaned_data(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.validationError('Password incorrect')
        elif len(password2) < 8:
            raise forms.validationError('passoord is less than 8 char')
        return password1



