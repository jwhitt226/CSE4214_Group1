from django.shortcuts import render, get_object_or_404
from .compare import Compare
from store.models import Inventory
from store.models import Customer
from django.http import JsonResponse


def compare(request):
    if request.user.is_authenticated:
        user = Customer.objects.get(userID=request.user)
    compare = Compare(request)
    compare_books = compare.get_compare
    return render(request, "compare.html", {"compare_books":compare_books, 'customer': user})





def compareAdd(request):
    compare = Compare(request)

    if request.POST.get('action') == 'post':
        book_ID = int(request.POST.get('books_ISBN'))

        book = get_object_or_404(Inventory, id=book_ID)

        compare.add(book=book)

        response = JsonResponse({'Product Name: ': book.title})
        return response

def compareDelete(request):
        compare = Compare(request)
        if request.POST.get('action') == 'post' :

            book = int(request.POST.get('books_ID'))

            compare.delete(book=book)

            response = JsonResponse({'Product Name: ': book})
            return response

# Create your views here.
