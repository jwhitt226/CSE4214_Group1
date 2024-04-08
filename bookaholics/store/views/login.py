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
from store.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #this needs to be cleaned up and given a message
            #messages.success(request, "Successfully logged in")
            return redirect('browse')
        else:
#            messages.error(request, "Invalid credentials")
            return redirect('login')

    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('welcome')