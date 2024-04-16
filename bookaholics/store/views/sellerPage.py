from django.shortcuts import render
from ..models import Inventory

def sellerPage(request):
    current_user = request.user
    sellerListings = Inventory.objects.filter(sellerID = current_user)

    return render(request, 'sellerPage.html', {'books': sellerListings})