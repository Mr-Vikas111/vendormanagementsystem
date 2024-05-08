from django.contrib import admin
from vendor.models import base as base_vendor_models
# Register your models here.

@admin.register(base_vendor_models.VendorData)
class VenderAdmin(admin.ModelAdmin):
    list_display = ['id','name','vendor_code','created']

    search_fields = ('name','vendor_code')
    list_filter = ['vendor_code','fulfillment_rate']
    list_display_links = ["vendor_code",'name']
    ordering = ('-created',)