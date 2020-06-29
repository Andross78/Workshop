from django import forms
from django.core.validators import EmailValidator, validate_email
from django.contrib.auth.forms import UserCreationForm
from pancar.models import User

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

# class UserCreateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         widgets = {'email': forms.TextInput(attrs={'placeholder': 'Email',}),
#                    'password': forms.TextInput( attrs={'placeholder': 'Haslo'})}
#         labels = {
#             "email": "",
#             "password": "",
#         }
#
# class UserCreateForm(forms.ModelForm):
#     class Meta:
#         model =  get_user_model()
#         fields = ['email','password','first_name','last_name']
#         widgets = {'password':forms.PasswordInput}
#     confirm_password = forms.CharField(widget=forms.PasswordInput())


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email',}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Haslo',}),
        }
        labels = {
            "email": "",
            "password": "",
        }