from django import forms
from django.contrib.auth import models
from django.db.models import fields
from .models import advertisement, image, comment



class advertisementForm(forms.ModelForm):
    class Meta:
        model = advertisement
        fields = ['rent','size','bedroom','bathroom','area','address','phone_number','cover_photo']

class imageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['image']

class commentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':10}))
    class Meta:
        model=comment
        fields = ['comment']