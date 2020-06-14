from django import forms
from django.core.validators import EmailValidator, validate_email
from pancar.models import User

# def valid_phone(phone):
#     if str(phone[0:3]) != '+48':
#         raise forms.ValidationError('Numer powinien zaczynac sie od +48')

class MessageForm(forms.Form):
    name = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    phone = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Telefonu'}))
    mail = forms.CharField(validators=[validate_email,], label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Password'}))
