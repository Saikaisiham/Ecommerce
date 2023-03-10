from django.urls import path
from .views import (
    home,
    CheckoutView,
    product,
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummery,
    remove_single_item_from_cart,
    PaymentView,
)

app_name =  'base'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('product/<slug>',ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart'),
    path('remove_single_item_from_cart/<slug>/',remove_single_item_from_cart,name='remove_single_item_from_cart'),
    path('order-summary/',OrderSummery.as_view(),name='order-summary')

    
]