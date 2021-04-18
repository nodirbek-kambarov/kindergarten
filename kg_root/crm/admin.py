from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'order_phone', 'order_dt']
