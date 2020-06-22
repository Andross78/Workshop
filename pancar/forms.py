from django import forms
from django.core.validators import EmailValidator, validate_email
from pancar.models import User

# def valid_phone(phone):
#     if str(phone[0:3]) != '+48':
#         raise forms.ValidationError('Numer powinien zaczynac sie od +48')

class MessageForm(forms.Form):
    name = forms.CharField(max_length=64, label='', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    phone = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Telefon'}))
    mail = forms.CharField(validators=[validate_email,], label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    info = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Informacja dla nas'}))

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username', }),
                   'password': forms.TextInput(attrs={'placeholder': 'Password'})}
        labels = {
            "username": "",
            "password": "",
        }

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'email': forms.TextInput(attrs={'placeholder': 'Email',}),
                   'password': forms.TextInput( attrs={'placeholder': 'Haslo'})}
        labels = {
            "email": "",
            "password": "",
        }