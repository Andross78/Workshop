from django import forms
import datetime
from pancar.models import Car, Cart, User


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'registration', 'year', 'review_date']


class OrderMailForm(forms.Form):
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))
    order_date = forms.CharField(widget=forms.HiddenInput(), initial=datetime.datetime.now())