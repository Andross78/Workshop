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
        fields = ['brand', 'model', 'registration', 'year', 'insurance', 'review_date', 'vin']
        labels = {
            'brand': '',
            'model': '',
            'registration': '',
            'year':'',
            'insurance': '',
            'review_date': '',
            'vin': '',
        }
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Marka:'}),
            'model': forms.TextInput(attrs={'placeholder': 'Model:'}),
            'registration': forms.TextInput(attrs={'placeholder': 'Nr rejestracyjny:'}),
            'year': forms.TextInput(attrs={'placeholder': 'Rok produkcji:'}),
            'insurance': forms.TextInput(attrs={'placeholder': 'Ubezpieczenie:',                                
                                                'onfocus': '(this.type="date")'}),
            'review_date': forms.TextInput(attrs={'placeholder': 'Przeglad techniczny:',                            
                                                'onfocus': '(this.type="date")'}),
            'vin': forms.TextInput(attrs={'placeholder': 'VIN:'}),
        }


class CarUpdateForm(forms.Form):

    brand = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'brand_edit','placeholder': 'Marka:'}))
    model = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'model_edit','placeholder': 'Model:'}))
    registration = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'registration_edit','placeholder': 'Nr rejestracyjny:'}))
    year = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'year_edit','placeholder': 'Rok produkcji:'}))
    insurance = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'insurance_edit','placeholder': 'Ubezpieczenie:', 'onfocus': '(this.type="date")',}))
    review_date = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'review_date_edit','placeholder': 'Przeglad techniczny:', 'onfocus': '(this.type="date")',}))
    vin = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'vin_edit','placeholder': 'VIN:'}))


class OrderMailForm(forms.Form):
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))
    order_date = forms.CharField(widget=forms.HiddenInput(), initial=datetime.datetime.now())


class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), required=False)