from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('experts/', views.experts, name= 'experts'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    
] 
