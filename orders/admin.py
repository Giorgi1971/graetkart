from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number', 'full_name', 'email', 'phone', 'city',
        'tax', 'order_total', 'status', 'is_ordered', 'created_at'
    ]
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'email', 'phone']
    list_per_page = 20


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
