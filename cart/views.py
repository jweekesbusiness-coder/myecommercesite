from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from myapp.models import Product
from .cart import Cart

# Create your views here.
def cart_add(request):
    cart = Cart(request)
    print("Add to cart button")
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to cart has id ",product_id)
        print("Product quantity is: ",product_quantity)
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product, product_qty = product_quantity )
        cart_quantity = cart.__len__()
        print(cart)
    return JsonResponse({"qty":cart_quantity})


def cart_overview(request):
    cart = Cart(request)
    return render(request,"cart/cart-overview.html",{"cart":cart})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        return JsonResponse({'qty':cart_quantity,'total':cart_total})
    return JsonResponse({'message':"Item was not deleted"})

def cart_update(request):
    cart = Cart(request)
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        cart.update(product__id=product_id,qty = product_quantity)
        return JsonResponse({'message','product updated'})