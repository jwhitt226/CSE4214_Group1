from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare, name="compare"),
    path('add/', views.compareAdd, name="compareAdd"),
    path('delete/', views.compareDelete, name="compareDelete"),
]