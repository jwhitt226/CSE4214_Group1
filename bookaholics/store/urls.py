from django.contrib import admin
from django.urls import path
from .views.welcome import welcome
from .views.listing import browse
from .views.listing import viewListing
from .views.cart import Cart  # Import the Cart view
from .views.checkout import Checkout
from .views.signup import signUp_user
from .views.login import login_user, logout_user


#from .views.home import Index , store
#from .views.signup import Signup
#from .views.login import Login, logout
#from .views.cart import Cart
#from .views.checkout import CheckOut
#from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', welcome, name='welcome'),
    #have to adjust this to "viewListing/<int:pk>"
    path('browse/', browse, name='browse'),
    path('viewListing/<int:pk>', viewListing, name='viewListing'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', Checkout.as_view() , name='checkout'),
    path('signUp/', signUp_user, name='signUp'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
#    path('', Index.as_view(), name='homepage'),
#    path('store', store , name='store'),

#    path('signup', Signup.as_view(), name='signup'),
#    path('login', Login.as_view(), name='login'),
#    path('logout', logout , name='logout'),
#    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
#    path('check-out', CheckOut.as_view() , name='checkout'),
#    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]