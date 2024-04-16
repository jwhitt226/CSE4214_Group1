from django.contrib import admin
from django.urls import path
from .views.welcome import welcome
from .views.listing import browse
from .views.listing import viewListing
from .views.login import login_user, logout_user, register_user, accountOptions
from .views.addListing import processaddListing
from .views.sellerPage import sellerPage

urlpatterns = [
    path('', welcome, name='welcome'),
    #have to adjust this to "viewListing/<int:pk>"
    path('browse/', browse, name='browse'),
    path('viewListing/<int:pk>', viewListing, name='viewListing'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('accountOptions/', accountOptions, name='accountOptions'),
    path('addListing/', processaddListing, name='processaddListing'),
    path('sellerPage/', sellerPage, name='sellerPage')
]