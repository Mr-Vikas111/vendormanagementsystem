from vendor.models import base as base_vendor_models



class VendorFunctions:

    def all_vendors():
        """
        return all vendors queryset
        """
        return base_vendor_models.VendorData.objects.all()
    
    def get_vendor(id):
        """
        return single vendor obj
        """
        return base_vendor_models.VendorData.objects.get(id=id)