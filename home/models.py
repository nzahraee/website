from django.db import models
from django.contrib.auth.models import User



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name



class product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(blank=True,null=True)
    unite_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name


    @property
    def total_price(self):
        if not self.discount:
            return self.unite_price
        elif self.discount:
            total = (self.discount * self.unite_price)/100
            return int(self.unite_price - total)
        return self.total_price

