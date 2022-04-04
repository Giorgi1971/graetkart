from django.contrib import admin

from carts.views import cart
from .models import *



admin.site.register(Cart)
admin.site.register(CartItem)