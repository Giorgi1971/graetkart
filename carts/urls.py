from . import views
from django.urls import path


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart_item/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),  # different in UDEMY
    path('minus_cart_item/<int:cart_item_id>/', views.minus_cart_item, name='minus_cart_item'),  # different in UDEMY.

    path('checkout/', views.checkout, name='checkout'),
] 
