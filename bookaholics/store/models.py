from typing import Iterable
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager

"""
#Models
#class modelName(models.Model):
    #Fields


    def __str__(self):
#        return self.primaryKey
    
    def get_absolute_url(self):
#        return reverse('model-detail-view', args = [str(self.id)])
        
    class Meta:
#        ordering = [Ordering Method]
"""

#Models
##Accounts

class CustomUserManager(BaseUserManager):
    def create_user(self, userID, email, password=None, **extra_fields):
        if not userID:
            raise ValueError('The User ID must be set')
        if not email:
            raise ValueError('The Email must be set')

        user = self.model(
            userID = userID,
            email = self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, userID, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        return self.create_user(userID, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        SELLER = "SELLER", "Seller"
        ADMIN = "ADMIN", "Admin"
    
    userID = models.CharField(max_length = 50, unique=True, default = 'userID')
    email = models.EmailField(max_length = 50, unique=True)
    type = models.CharField(max_length = 50, choices = Types.choices, default = Types.CUSTOMER)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'userID'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = [EMAIL_FIELD]

    objects = CustomUserManager()

    def __str__(self):
        return self.userID
    
class Customer(models.Model):
    userID = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    fname = models.CharField(max_length = 20, blank = True)
    lname = models.CharField(max_length = 50, blank = True)
    address = models.CharField(max_length = 100, blank = True)
    credit = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)

    # def __str__(self):
    #     return self.userID

class Seller(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        DENIED = "DENIED", "Denied"

    sellerID = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 50, blank = True)
    address = models.CharField(max_length = 100, blank = True)
    status = models.CharField(max_length = 20, choices = Status.choices, default = Status.PENDING)
    credit = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)

    # def __str__(self):
    #     return self.userID

def create_more(sender, instance, created, **kwargs):
    if created:
        if instance.type == User.Types.CUSTOMER:
            customer = Customer(userID = instance)
            customer.save()
        elif instance.type == User.Types.SELLER:
            seller = Seller(sellerID = instance)
            seller.save()

post_save.connect(create_more, sender = User)

##Account Management & Order History
class SellerReq(models.Model):
    #Fields
    requestID = models.IntegerField(primary_key = True)
    sellerID = models.ForeignKey('User', on_delete=models.RESTRICT)
    status = models.CharField(max_length = 15)
    dateApplied = models.DateField(auto_now_add = True)
    
    def __int__(self):
        return self.requestID
    
    def get_absolute_url(self):
        return reverse('sellerReq-detail-view', args = [str(self.id)])
    
    #Metadata
    class Meta:
        ordering = ['dateApplied']

##Inventory Management
class Inventory(models.Model):
    #Fields
    id = models.BigAutoField(primary_key = True)
    sellerID = models.ForeignKey('User', on_delete=models.CASCADE)
    isbn = models.IntegerField()
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to = 'inventory_images/', default = 'inventory_images/default.jpg')
    
    def __int__(self):
        return self.id
    
    def get_absolute_url(self):
        return reverse('inventory-detail-view', args = [str(self.id)])
    
    #Metadata
    class Meta:
        ordering = ['id']

class ShoppingCart(models.Model):
    #Fields
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    itemID = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name = 'itemID_cart')
    quantity = models.IntegerField()
    price = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name = 'price_cart')
    
    def __str__(self):
        return self.userID
    
    def get_absolute_url(self):
        return reverse('shoppingCart-detail-view', args = [str(self.id)])
        
    #Metadata
    class Meta:
        ordering = ['userID']
    
class OrderHist(models.Model):
    #Fields
    orderID = models.IntegerField(primary_key = True)
    userID = models.ForeignKey('User', on_delete=models.RESTRICT)
    itemID = models.ForeignKey('Inventory', on_delete=models.RESTRICT, related_name = 'itemID_sold')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    dateOrdered = models.DateField(auto_now_add = True)
    
    def __int__(self):
        return self.orderID
    
    def get_absolute_url(self):
        return reverse('prevsold-detail-view', args = [str(self.orderID)])
        
    #Metadata
    class Meta:
        ordering = ['orderID']