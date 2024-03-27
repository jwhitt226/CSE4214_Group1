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
        zip_code = postData.get('zip')
        
#validate
        value = { 
            'email': email,
            'password': password,
            'first_name': first_name, 
            'last_name': last_name,
            'address': address,
            'state': state,
            'city': city,
            'zip': zip_code
        }

        admin_code = postData.get('Admin Code')
        is_admin = False
        if admin_code == 'Your Admin Code':
            is_admin = True

        user = User.objects.create_user(email = email, 
                                        password = password,
                                        first_name = first_name,
                                        last_name = last_name)
        user.save()

        if user:
            if is_admin:
                admin = Admin.objects.create(user = user,
                                             address = address,
                                             state = state,
                                             city = city,
                                             zip_code = zip_code)
            else:
                seller = Seller.objects.create(user = user,
                                               address = address,
                                               state = state,
                                               city = city,
                                               zip_code = zip_code)
            return redirect('login.html')
        
        return render(request,'signup.html',{'Failed to create user'})
