from django.contrib import admin

from .models import OnlineOrder

@admin.register(OnlineOrder)
class OnlineOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer_email', 'customer_name', 'status', 'subtotal', 'created_at']
    search_fields = ['order_number', 'customer_email', 'customer_name', 'status']
    readonly_fields = ['created_at', 'updated_at']

