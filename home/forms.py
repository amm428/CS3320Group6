from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #^encrypt password

    # Meta is info about class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']