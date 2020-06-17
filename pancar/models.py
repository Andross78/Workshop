from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20)

    def get_cart(self):
        try:
            cart = Cart.objects.get(user=self)
        except Exception as e:
            cart = Cart.objects.create(user=self)
        return cart


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    registration = models.CharField(max_length=16)
    year = models.IntegerField()
    review_date = models.DateTimeField(null=True)
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

    def confirm(self):
        # send main
        # zamiana statusu
        # :)
        pass