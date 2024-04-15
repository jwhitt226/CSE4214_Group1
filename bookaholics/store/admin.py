from django.contrib import admin
#from django.contrib.auth.models import User
from .models import User, Customer, Seller, SellerReq, OrderHist, Inventory, ShoppingCart

# Register your models here.
#admin.site.register(Admin)
#admin.site.register(Seller)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(SellerReq)
admin.site.register(OrderHist)
admin.site.register(Inventory)
admin.site.register(ShoppingCart)
