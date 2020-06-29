from django import forms
import datetime
from pancar.models import Car, User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email']
        labels = {
            'first_name': '',
            'last_name': '',
            'phone': '',
            'email': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
        }

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'registration', 'year', 'insurance', 'review_date']
        labels = {
            'brand': '',
            'model': '',
            'registration': '',
            'year':'',
            'insurance': '',
            'review_date': '',
        }
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Marka:'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model:'}),
            'registration': forms.TextInput(attrs={'placeholder': 'Nr rejestracyjny:'}),
            'year': forms.TextInput(attrs={'placeholder': 'Rok produkcji:'}),
            'insurance': forms.TextInput(attrs={'placeholder': 'Ubezpieczenie:'}),
            'review_date': forms.TextInput(attrs={'placeholder': 'Przeglad techniczny:'}),
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'registration', 'year', 'insurance', 'review_date']
        labels = {
            'brand': '',
            'model': '',
            'registration': '',
            'year':'',
            'insurance': '',
            'review_date': '',
        }
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Marka:'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model:'}),
            'registration': forms.TextInput(attrs={'placeholder': 'Nr rejestracyjny:'}),
            'year': forms.TextInput(attrs={'placeholder': 'Rok produkcji:'}),
            'insurance': forms.TextInput(attrs={'placeholder': 'Ubezpieczenie:'}),
            'review_date': forms.TextInput(attrs={'placeholder': 'Przeglad techniczny:'}),
        }

class OrderMailForm(forms.Form):
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))
    order_date = forms.CharField(widget=forms.HiddenInput(), initial=datetime.datetime.now())