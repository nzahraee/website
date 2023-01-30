from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category',null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug, self.id])


    '''def get_absolute_url(self):
        return reverse('home:category',args=[self.slug,self.id])
'''

class product(models.Model):
    variant = (
        ('None', 'none'),
        ('Size', 'size'),
        ('Color', 'color'),
    )
    category = models.ManyToManyField(Category,blank=True)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    unite_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField(blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    status = models.CharField(null=True,blank=True,max_length=200, choices=variant)
    image = models.ImageField(upload_to='product',null=True,blank=True)

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

class size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class color(models.Model):
    name = models.CharField( max_length=200)

    def __str__(self):
        return self.name

class Variants(models.Model):
    name = models.CharField(max_length=100)
    product_variant = models.ForeignKey(product,on_delete=models.CASCADE)
    size_variant = models.ForeignKey(size,on_delete=models.CASCADE)
    color_variant = models.ForeignKey(color,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unite_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()

    @property
    def total_price(self):
        if not self.discount:
            return self.unite_price
        elif self.discount:
            total = (self.discount * self.unite_price) / 100
            return int(self.unite_price - total)
        return self.total_price


