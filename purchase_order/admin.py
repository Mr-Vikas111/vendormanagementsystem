from django.contrib import admin
from purchase_order.models import base as  base_purchase_order_models
# Register your models here.

@admin.register(base_purchase_order_models.PurchaseOrderData)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id','po_number','vendor','order_date','created']

    search_fields = ('name','po_number')
    list_filter = ['po_number','vendor']
    list_display_links = ['po_number']
    ordering = ('-created',)

@admin.register(base_purchase_order_models.VendorPerformanceData)
class VendorPerformanceDataAdmin(admin.ModelAdmin):
    list_display = ['id','vendor','date','created']

    list_filter = ['date','vendor']
    list_display_links = ['vendor']
    ordering = ('-created',)
