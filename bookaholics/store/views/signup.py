from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from form import SignUpForm
from django.contrib import messages

#class signUp(View):
#    def get(self, request):
#        return render(request, 'signUp.html')
    
#    def post(self,request):
#        postData = request.POST
#        email = postData.get('email')
#        password = postData.get('password')
#        first_name = postData.get('firstname')
#        last_name = postData.get('lastname')
#        address = postData.get('address')
#        state = postData.get('state')
#        city = postData.get('city')
#        zip_code = postData.get('zip')
        
#validate
#        value = { 
#            'email': email,
#            'password': password,
#            'first_name': first_name, 
#            'last_name': last_name,
#            'address': address,
#            'state': state,
#            'city': city,
#            'zip': zip_code
#        }

#        admin_code = postData.get('Admin Code')
#        is_admin = False
#        if admin_code == 'Your Admin Code':
#            is_admin = True

#        user = User.objects.create_user(email = email, 
#                                        password = password,
#                                        first_name = first_name,
#                                        last_name = last_name)
#        user.save()

#        if user:
#            if is_admin:
#                admin = Admin.objects.create(user = user,
#                                             address = address,
#                                             state = state,
#                                             city = city,
#                                             zip_code = zip_code)
#            else:
#                seller = Seller.objects.create(user = user,
#                                               address = address,
#                                               state = state,
#                                               city = city,
#                                               zip_code = zip_code)
                
#                user = authenticate(request, email=email, password=password)
#            if user is not None:
#                login(request, user)
#                return redirect('welcome')  # Redirect to the home page
#            else:
#                return render(request, 'signUp.html', {'error': 'Failed to authenticate user'})

#        return render(request, 'signUp.html', {'error': 'Failed to create user'})
    
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully Registered!")
            return(redirect, 'browse')
        else:
            messages.success(request, "Registration Failed! Please Try Again.")
            return(redirect, 'signUp')
    return render(request, 'signUp.html', {'form':form})   
