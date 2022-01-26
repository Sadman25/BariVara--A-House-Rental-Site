from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('createAdvertisement',views.createAdvertisement, name='createAdvertisement'),
    path('advertisementDetails/<int:pk>/',views.advertisementDetails, name='advertisementDetails'),
    path('advertisementEdit/<int:pk>/',views.advertisementEdit, name='advertisementEdit'),
    path('advertisementDelete/<int:pk>/', views.advertisementDelete, name='advertisementDelete'),
    path('myAdvertisements',views.myAdvertisements,name='myAdvertisements'),
    path('searchByArea',views.searchByArea,name='searchByArea'),

    path('myProfile/<int:pk>/',views.myProfile, name='myProfile'),
    
]