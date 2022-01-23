from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class profile (models.Model):
    user = models.OneToOneField(User,null=False,blank=False, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=False,blank=False)


    def __str__(self) -> str:
        return self.user.username