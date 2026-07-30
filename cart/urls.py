from django.urls import path
from . import views

urlpatterns = [
    path('add',views.cart_add,name="cart_add"),
    path('delete',views.cart_delete,name='cart_delete'),
    path('cart-overview',views.cart_overview,name='cart-overview'),
    path('update',views.cart_update,name='cart_update'),
]
