# from django.shortcuts import render , redirect , HttpResponseRedirect
# from django.contrib.auth.hashers import  check_password
# from store.models import User
# from django.views import View


# class Login(View):
#     return_url = None

#     def get(self, request):
#         Login.return_url = request.GET.get ('return_url')
#         return render (request, 'login.html')

#     def post(self, request):
#         email = request.POST.get ('email')
#         password = request.POST.get ('password')
#         user = User.get_user_by_email (email)
#         error_message = None
#         if user:
#             flag = check_password (password, user.password)
#             if flag:
#                 request.session['user'] = user.id

#                 if Login.return_url:
#                     return HttpResponseRedirect (Login.return_url)
#                 else:
#                     Login.return_url = None
#                     return redirect ('homepage')
#             else:
#                 error_message = 'Invalid email address or password. Try again. '
#         else:
#             error_message = 'Invalid email address or password. Try again.'

#         print (email, password)
#         return render (request, 'login.html', {'error': error_message})

# def logout(request):
#     request.session.clear()
#     return redirect('login')

from django.shortcuts import render, redirect
from store.models import User, Customer, Seller
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from store.forms import SignUpForm, CustomerSignUpForm, SellerSignUpForm

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            #this needs to be cleaned up and given a message
            #messages.success(request, "Successfully logged in")
            role = user.type
            if role == "CUSTOMER":
                return redirect('accountOptions')
            elif role == "SELLER":
                return redirect('accountOptions')
            return redirect('login')
        else:
            messages.success(request, "Invalid credentials")
            return redirect('login')

    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('welcome')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('userID')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account created! Welcome!")
            return redirect('accountOptions')
        else:
            messages.success(request, "Invalid credentials")
            return redirect('register')
    else:
        return render(request, 'signUp.html', {'form': form})
    
    
def accountOptions(request):
    if request.user.is_authenticated:
        if request.user.type == "CUSTOMER":
            current_user = Customer.objects.get(userID_id=request.user.id)
            form = CustomerSignUpForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, "Customer Account Created! Welcome!")
                return redirect('browse')
            return render(request, 'customerAccount.html', {'form': form})
        elif request.user.type == "SELLER":
            current_user = Seller.objects.get(sellerID_id=request.user.id)
            form = SellerSignUpForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, "Seller Account Created! Welcome!")
                return redirect('browse')
            return render(request, 'customerAccount.html', {'form': form})
    else:
        messages.success(request, "You are not logged in")
        return redirect('login')