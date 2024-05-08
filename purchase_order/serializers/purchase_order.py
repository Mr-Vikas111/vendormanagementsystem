from rest_framework import serializers 
from purchase_order.models import base as base_purchase_order_models
from helper.serializers import BaseSerializer

class POListSerializer(BaseSerializer):
    class Meta:
        model = base_purchase_order_models.PurchaseOrderData
        exclude =['created','modified']

class PODetailSerializer(BaseSerializer):
    class Meta:
        model = base_purchase_order_models.PurchaseOrderData
        exclude =['created','modified']

class POCreateSerializers(BaseSerializer):
    class Meta:
        model = base_purchase_order_models.PurchaseOrderData
        exclude = ['created','modified']
