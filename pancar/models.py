from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    phone = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('profile')

    def get_cart(self):
        try:
            cart = Cart.objects.get(user=self)
        except Exception as e:
            cart = Cart.objects.create(user=self)
        return cart

    def get_ordered_cart(self):
        try:
            ordered_cart = OrderedCart.objects.get(user=self)
        except Exception as e:
            ordered_cart = OrderedCart.objects.create(user=self)
        return ordered_cart

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email

class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    registration = models.CharField(max_length=16)
    year = models.IntegerField()
    review_date = models.DateTimeField(null=True)
    insurance = models.DateTimeField(null=True)
    vin = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cars')

    def __str__(self):
        return self.brand + ' ' + self.model


class Process(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    category = models.ManyToManyField('Category', related_name='processes')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    process = models.ManyToManyField(Process, related_name='carts')

    def __str__(self):
        return "Cart of {}, #{}".format(User, self.id)

    def get_total_price(self):
        processes = Process.objects.filter(carts=self)
        tot_price = 0
        for proc in processes:
            tot_price += proc.price
        return tot_price

class OrderedCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordered_carts')
    process = models.ManyToManyField(Process, related_name='ordered_carts')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Zamowione uslugi {} ({}) ".format(self.user, self.id)

    def get_total_amount(self):
        processes = Process.objects.filter(ordered_carts=self)
        tot_price = 0
        for proc in processes:
            tot_price += proc.price
        return tot_price