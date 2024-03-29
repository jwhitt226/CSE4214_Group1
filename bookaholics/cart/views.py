from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, "cart.html")

def cartAdd(request):
    pass

def cartDelete(request):
    pass

def cartUpdate(request):
    pass