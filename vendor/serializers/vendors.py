from rest_framework import serializers 
from vendor.models import base as base_vendor_models
from helper.serializers import BaseSerializer

class VendorsListSerializer(BaseSerializer):
    class Meta:
        model = base_vendor_models.VendorData
        exclude =['created','modified']

class VendorsDetailSerializer(BaseSerializer):
    class Meta:
        model = base_vendor_models.VendorData
        exclude =['created','modified']

class VendorsCreateSerializers(BaseSerializer):
    class Meta:
        model = base_vendor_models.VendorData
        exclude = ['created','modified']
