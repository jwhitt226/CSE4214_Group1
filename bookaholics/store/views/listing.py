from django.shortcuts import render
from ..models import Inventory

def browse(request):

    books = Inventory.objects.all()

    return render(request, 'userPage.html', {'books': books})


def viewListing(request, pk):
    
    #Get book information from Inventory
    book = Inventory.objects.get(pk=pk)

    return render(request, 'veiw_listing.html', {'book': book})