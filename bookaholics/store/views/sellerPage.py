from django.shortcuts import render
from ..models import Inventory
from ..models import Seller

def sellerPage(request):
    if request.user.is_authenticated:
        user = Seller.objects.get(sellerID=request.user)
    current_user = request.user
    sellerListings = Inventory.objects.filter(sellerID = current_user)

    return render(request, 'sellerPage.html', {'books': sellerListings, 'seller': user})

def viewSellerListing(request, pk):
    if request.user.is_authenticated:
        user = Seller.objects.get(sellerID=request.user)
    
    #Get book information from Inventory
    book = Inventory.objects.get(id=pk)

    return render(request, 'viewSellerListing.html', {'book': book, 'seller': user})

def delete(request, pk):
    book = Inventory.objects.get(id=pk)
    book.delete()

    return sellerPage(request)