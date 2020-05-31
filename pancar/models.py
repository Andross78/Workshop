from django.db import models

# Create your models here.

class Klient(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname

class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    registration = models.CharField(max_length=16)
    year = models.IntegerField()
    owner = models.ForeignKey(Klient, on_delete=models.CASCADE, null=True)

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