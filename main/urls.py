from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('prices', views.prices),
    path('contact', views.contact)
]
