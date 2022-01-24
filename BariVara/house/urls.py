from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('createAdvertisement',views.createAdvertisement, name='createAdvertisement'),
    path('advertisementDetails/<int:pk>/',views.advertisementDetails, name='advertisementDetails'),
    path('myAdvertisements',views.myAdvertisements,name='myAdvertisements'),

    path('myProfile/<int:pk>/',views.myProfile, name='myProfile'),
    
]