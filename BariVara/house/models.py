from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class area (models.Model):
    area = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.area

class advertisement(models.Model):
    area = models.ForeignKey(area,null=True,on_delete= models.SET_NULL)
    address=models.CharField(max_length=100)
    bedroom=models.PositiveIntegerField()
    bathroom=models.PositiveIntegerField()
    rent=models.PositiveIntegerField()
    size=models.PositiveIntegerField()
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    cover_photo= models.ImageField(blank=False, null=False)
    phone_number=models.CharField(max_length=11)

    def __str__(self) -> str:
        return 'Location: '+self.area.area + ' Owner: '+ self.owner.username + ' Number '+ self.phone_number
    
    def get_absolute_url(self):
        return reverse('advertisementDetails', kwargs={'pk':self.id})

class image(models.Model):
    advertisement= models.ForeignKey(advertisement,on_delete=models.CASCADE)
    image= models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.advertisement.owner.username

class comment(models.Model):
    advertisement= models.ForeignKey(advertisement,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete= models.CASCADE)
    reply = models.ForeignKey('comment' , null=True , related_name = "replies" , on_delete = models.CASCADE)
    comment= models.TextField(max_length=5000,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True,null=False)