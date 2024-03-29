from django.contrib import admin
from django.urls import path
from .views.welcome import welcome
from .views.listing import browse
from .views.listing import viewListing

urlpatterns = [
    path('', welcome, name='welcome'),
    #have to adjust this to "viewListing/<int:pk>"
    path('browse/', browse, name='browse'),
    path('viewListing/<int:pk>', viewListing, name='viewListing'),
]