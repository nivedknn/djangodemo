from os import name

from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    data_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Product,name


    def subtotal(self):
        return self.quantity*self.product.price

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address=models.TextField()
    phone=models.IntegerField()
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=20,default="pending")
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Account(models.Model):
    accnum=models.IntegerField()
    acctyp=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return self.accnum