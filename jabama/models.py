from django.db import models
from django.contrib.auth.models import User


class acomodation(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='acomodation',null=True,blank=True)
    desc = models.CharField(max_length=300,null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update = models.DateTimeField(auto_now=True,null=True,blank=True)
    avail = models.BooleanField(default=True,null=True,blank=True)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField(blank=True,null=True)



    def __str__(self):
        return self.name




