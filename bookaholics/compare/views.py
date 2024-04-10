from django.shortcuts import render, get_object_or_404
from .compare import Compare
from store.models import Inventory
from django.http import JsonResponse


def compare(request):
    compare = Compare(request)
    compare_books = compare.get_compare
    return render(request, "compare.html", {"compare_books":compare_books})





def compareAdd(request):
    compare = Compare(request)

    if request.POST.get('action') == 'post':
        book_ISBN = int(request.POST.get('books_ISBN'))

        book = get_object_or_404(Inventory, isbn=book_ISBN)

        compare.add(book=book)

        response = JsonResponse({'Product Name: ': book.title})
        return response

def compareDelete(request):
    pass

def compareUpdate(request):
    pass

# Create your views here.
