from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models import Inventory
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        inventory = request.POST.get('inventory')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(inventory)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(inventory)
                    else:
                        cart[inventory]  = quantity-1
                else:
                    cart[inventory]  = quantity+1

            else:
                cart[inventory] = 1
        else:
            cart = {}
            cart[inventory] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    inventory = None
    products = Inventory.get_all_products();

    data = {}
    data['inventory'] = inventory

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


