from typing import Iterable
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
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
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        SELLER = "SELLER", 'Seller'

    base_role = Role.ADMIN

    role = models.CharField(max_length = 50, choices = Role.choices, default = base_role)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = User.Role.CUSTOMER)

class Customer(User):
    
    base_role = User.Role.CUSTOMER

    customer = CustomerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, valued customer!"

@receiver(post_save, sender=Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user = instance)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    userID = models.IntegerField(null=True, blank=True)

class SellerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role = User.Role.SELLER)

class Seller(User):
    
    base_role = User.Role.SELLER

    seller = SellerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, valued seller!"
    
@receiver(post_save, sender=Seller)
def create_seller_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SELLER":
        SellerProfile.objects.create(user = instance)

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    sellerID = models.IntegerField(null=True, blank=True)


# class Admin(models.Model):
#     #Fields
#     adminID = models.IntegerField(primary_key = True)
#     password = models.CharField(max_length = 20, help_text = 'Enter Password')
#     fname = models.CharField(max_length = 20, help_text = 'Enter First Name')
#     lname = models.CharField(max_length = 20, help_text = 'Enter Last Name')
#     email = models.EmailField(max_length = 40, help_text = 'Enter Email Address')

#     def __int__(self):
#         return self.adminID
    
#     def get_absolute_url(self):
#         return reverse('admin-detail-view', args = [str(self.id)])
        
#     #Metadata
#     class Meta:
#         ordering = ['adminID']
        
# class Seller(models.Model):
#     #Fields
#     sellerID = models.IntegerField(primary_key = True)
#     password = models.CharField(max_length = 20, help_text = 'Enter Password')
#     name = models.CharField(max_length = 20, help_text = 'Enter Name')
#     email = models.EmailField(max_length = 40, help_text = 'Enter Email Address')
#     address = models.CharField(max_length = 50, help_text = 'Enter Address')
#     status = models.CharField(max_length = 10)
    
#     def __int__(self):
#         return self.sellerID
    
#     def get_absolute_url(self):
#         return reverse('seller-detail-view', args = [str(self.id)])
        
#     #Metadata
#     class Meta:
#         ordering = ['sellerID']

# class User(models.Model):
#     #Fields
#     userID = models.CharField(primary_key = True, max_length = 20, help_text = 'Enter Username')
#     password = models.CharField(max_length = 20, help_text = 'Enter Password')
#     fname = models.CharField(max_length = 20, help_text = 'Enter First Name')
#     lname = models.CharField(max_length = 20, help_text = 'Enter Last Name')
#     billAddr = models.CharField(max_length = 50, help_text = 'Enter Billing Address')
#     email = models.EmailField(max_length = 40, help_text = 'Enter Email Address')

#     def __str__(self):
#         return self.userID
    
#     def get_absolute_url(self):
#         return reverse('user-detail-view', args = [str(self.id)])

#     #Metadata
#     class Meta:
#         ordering = ['userID']
#         constraints = [
#             UniqueConstraint(
#                 Lower('userID'),
#                 name = 'userID_case_insensitive_unique',
#                 violation_error_message = "Username already exists"
#             )
#         ]


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

class OrderHist(models.Model):
    #Fields
    orderID = models.IntegerField(primary_key = True)
    userID = models.ForeignKey('User', on_delete=models.RESTRICT)
    dateOrdered = models.DateField(auto_now_add = True)
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    numItems = models.IntegerField()
    
    def __int__(self):
        return self.orderID
    
    def get_absolute_url(self):
        return reverse('orderHist-detail-view', args = [str(self.id)])
        
    #Metadata
    class Meta:
        ordering = ['dateOrdered']


##Inventory Management
class Inventory(models.Model):
    #Fields
    isbn = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to = 'inventory_images/', default = 'inventory_images/default.jpg')
    
    def __int__(self):
        return self.isbn
    
    def get_absolute_url(self):
        return reverse('inventory-detail-view', args = [str(self.id)])
    
    #Metadata
    class Meta:
        ordering = ['isbn']

class ShoppingCart(models.Model):
    #Fields
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    isbn = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name = 'isbn_cart')
    quantity = models.IntegerField()
    price = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name = 'price_cart')
    
    def __str__(self):
        return self.userID
    
    def get_absolute_url(self):
        return reverse('shoppingCart-detail-view', args = [str(self.id)])
        
    #Metadata
    class Meta:
        ordering = ['userID']
    
class PrevSold(models.Model):
    #Fields
    orderID = models.ForeignKey('OrderHist', on_delete=models.RESTRICT)
    userID = models.ForeignKey('User', on_delete=models.RESTRICT)
    isbn = models.ForeignKey('Inventory', on_delete=models.RESTRICT, related_name = 'isbn_sold')
    quantity = models.IntegerField()
    price = models.ForeignKey('Inventory', on_delete=models.RESTRICT, related_name = 'price_sold')
    
    def __int__(self):
        return self.orderID
    
    def get_absolute_url(self):
        return reverse('prevsold-detail-view', args = [str(self.id)])
        
    #Metadata
    class Meta:
        ordering = ['orderID']