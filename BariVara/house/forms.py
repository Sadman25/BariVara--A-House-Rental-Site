from django import forms
from django.contrib.auth import models
from django.db.models import fields
from .models import advertisement, image, comment



class advertisementForm(forms.ModelForm):
    class Meta:
        model = advertisement
        fields = ['rent','size','bedroom','bathroom','area','address','phone_number']

class imageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['image']