from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('createAdvertisement',views.createAdvertisement, name='createAdvertisement'),
    
]