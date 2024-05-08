from django.db import models
from vendor.models import base as  base_vendor_models
from helper.models import CreationModificationBase
from helper import keys


class PurchaseOrderData(CreationModificationBase):

    class StatusChoices(models.Choices):
        PENDING = keys.PENDING
        COMPLETED=keys.COMPLETED
        CANCELLED = keys.CANCELLED

    po_number = models.CharField(max_length=250,unique=True)
    vendor = models.ForeignKey(to=base_vendor_models.VendorData,on_delete=models.PROTECT,related_name='_po_vendor')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items= models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=30,choices=StatusChoices.choices)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date  = models.DateField(null=True)

    def __str__(self) -> str:
        return f'PO NO. -> {self.po_number},VENDOR -> {self.vendor}'
    

class VendorPerformanceData(CreationModificationBase):
    vendor = models.ForeignKey(to=base_vendor_models.VendorData,on_delete=models.PROTECT,related_name='_performance_vendor')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return f'VENDOR -> {self.vendor},DATE -> {self.date}'
