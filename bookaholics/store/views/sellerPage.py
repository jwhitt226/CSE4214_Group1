from django.shortcuts import render
from ..models import Inventory

def sellerPage(request):
    current_user = request.user
    sellerListings = Inventory.objects.filter(sellerID = current_user)

    return render(request, 'sellerPage.html', {'books': sellerListings})

def viewSellerListing(request, pk):
    
    #Get book information from Inventory
    book = Inventory.objects.get(id=pk)

    return render(request, 'viewSellerListing.html', {'book': book})

def delete(request, pk):
    book = Inventory.objects.get(id=pk)
    book.delete()

    return sellerPage(request)