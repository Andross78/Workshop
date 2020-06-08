from django import forms
from django.core.validators import EmailValidator, validate_email


def valid_phone(phone):
    if phone[0:3] != '+48':
        raise forms.ValidationError('Numer powinien zaczynac sie od +48')

class MessageForm(forms.Form):
    name = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    phone = forms.IntegerField(validators=[valid_phone,], label='', widget=forms.TextInput(attrs={'placeholder': 'Telefonu'}))
    mail = forms.CharField(validators=[validate_email,], label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))

