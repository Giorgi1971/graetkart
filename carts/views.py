from turtle import pen
from django.shortcuts import redirect, render
from carts.models import Cart, CartItem
from store.models import Product, Variation
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variation_categoru__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
                print(variation)
            except:
                pass


    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #get cart using catr_id prezent in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
    cart_item.save()

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = total*2/100
        grand_total = total+tax

    except CartItem.DoesNotExist:
        pass

    context = {'total':total, 'tax':tax, 'grand_total':grand_total, 'quantity':quantity, 'cart_items':cart_items}
    return render(request, 'store/cart.html', context)


# ეს სხვანაირადაა უდემზე. 
def remove_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


# ეს სხვანაირადაა უდემზე. 
def minus_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
