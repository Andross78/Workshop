from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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

    def send_confirm_email(self, request):
        from djoser.conf import settings as ds
        ae = ds.EMAIL.activation(request=request, context={'user':self})
        ae.send([self.email])

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email

class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    registration = models.CharField(max_length=16)
    year = models.IntegerField()
    review_date = models.DateField(null=True)
    insurance = models.DateField(null=True)
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
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Zamowione uslugi {} ({}) ".format(self.user, self.id)

    def get_total_amount(self):
        processes = Process.objects.filter(ordered_carts=self)
        tot_price = 0
        for proc in processes:
            tot_price += proc.price
        return tot_price


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)