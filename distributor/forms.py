from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Distributor
from django.contrib.auth.models import User


class DistributorCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    phone_number = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
