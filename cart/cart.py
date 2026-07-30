from myapp.models import Product
from decimal import Decimal
# Cart class for managing shopping cart functionality
class Cart():
    def __init__(self,request):
        self.session =    request.session #Get the session from the request
        cart = request.session.get('cart') #Get the cart from the session
        if 'cart' not in request.session:
               cart =  self.session['cart'] = {} #If the cart is not in the session, create an empty cart and store it in the session
        self.cart = cart

    def add(self, product, product_qty):
        product_id = product.id #Get the product id
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
              self.cart[product_id] = {'price':str(product.price),'qty': product_qty}   
        self.session.modified=True

    def delete(self,product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified=True

    def update(self, product__id, qty):
        product_id = str(product__id)
        product_quantity = qty

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        self.session.modified = True

    def __len__(self):
       return  sum(int(item['qty']) for item in self.cart.values())

    def get_total_price(self):
       return  sum(Decimal(item['price']) * Decimal(item['qty'])  for item in self.cart.values())

    #This method allows iteration over the items in the cart, yielding each item with its associated product, price, and total cost.
    def __iter__(self):
        product_ids =  self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
             cart[str(product.id)]['product'] = product

        for item in cart.values():
             item['price'] = Decimal(item['price'])
             item['total'] = item['price'] * Decimal(item['qty'])
             yield item

