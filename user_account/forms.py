from django import forms

from pancar.models import Car, User


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'registration', 'year', 'review_date']