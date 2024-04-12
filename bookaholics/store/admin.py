from django.contrib import admin
#from django.contrib.auth.models import User
from .models import User, CustomerMore, SellerMore, SellerReq, OrderHist, Inventory, ShoppingCart, PrevSold

# Register your models here.
#admin.site.register(Admin)
#admin.site.register(Seller)
admin.site.register(User)
admin.site.register(CustomerMore)
admin.site.register(SellerMore)
admin.site.register(SellerReq)
admin.site.register(OrderHist)
admin.site.register(Inventory)
admin.site.register(ShoppingCart)
admin.site.register(PrevSold)
