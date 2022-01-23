from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import profile


class userRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' ]
        help_texts = {
            'username': None,
            'email': None,
        }

class profileRegistration(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_picture']