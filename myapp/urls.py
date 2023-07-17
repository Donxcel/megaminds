# creating the various urls needed for our system
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_service/', views.add_service, name='add_service'),
    path('services/', views.ViewService, name='services'),
    path('projects/', views.ViewProject, name='projects'),

    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('index-2/', views.index_2, name='index_2'),
    path('index-3/', views.index_3, name='index_3'),
    path('index-4/', views.index_4, name='index_4'),



    #path('register', views.register, name='register'),
]