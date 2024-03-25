from django.contrib import admin
from .models import Admin, Seller, User, SellerReq, OrderHist, Inventory, ShoppingCart, PrevSold

# Register your models here.
admin.site.register(Admin)
admin.site.register(Seller)
admin.site.register(User)
admin.site.register(SellerReq)
admin.site.register(OrderHist)
admin.site.register(Inventory)
admin.site.register(ShoppingCart)
admin.site.register(PrevSold)
