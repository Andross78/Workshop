from django import forms

from pancar.models import Car, Cart


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'registration', 'year', 'review_date']


class CartCreateForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['process']