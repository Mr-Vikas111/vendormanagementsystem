from purchase_order.models import base as base_po_models



class POFunctions:

    def all_po():
        """
        return all vendors queryset
        """
        return base_po_models.PurchaseOrderData.objects.all()
    
    def get_po(id):
        """
        return single vendor obj
        """
        return base_po_models.PurchaseOrderData.objects.get(id=id)