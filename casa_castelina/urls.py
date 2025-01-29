from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('galeria/', views.galeria, name='galeria'),
    path('about/', views.about, name='about'),
    path('404/', views.not_found, name='not_found'),
]