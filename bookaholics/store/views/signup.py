import email
from django.shortcuts import render, redirect
from django.views import View
from bookaholics.store.models import Admin, Seller, User
from django.contrib.auth import authenticate, login

class signUp(View):
    def get(self, request):
        return render(request, 'signUp.html')
    
    def post(self,request):
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        address = postData.get('address')
        state = postData.get('state')
        city = postData.get('city')
        zip = postData.get('zip')
        
#validate
        value = { 
            'email': email,
            'password': password,
            'first_name': first_name, 
            'last_name': last_name,
            'address': address,
            'state': state,
            'city': city,
            'zip': zip
        }
