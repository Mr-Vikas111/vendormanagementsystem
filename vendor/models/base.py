from django.db import models
from helper.models import CreationModificationBase

class VendorData(CreationModificationBase):
    name = models.CharField(max_length=150)
    contact_detail = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=250,unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time  = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return f'VENDOR NAME ->{self.name},CODE -> {self.vendor_code}'