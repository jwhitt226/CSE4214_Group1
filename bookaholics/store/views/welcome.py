from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def logIn(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request, 'signUp.html')