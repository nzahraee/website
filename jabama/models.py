from django.db import models
from django.contrib.auth.models import User


class acomodation(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)




