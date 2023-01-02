from django.urls import path
from . import views

app_name = 'jabama'
urlpatterns = [
    path('jabama/',views.jabama, name='jabama'),
]