from django.urls import path
from vendor.apis import vendors as vendor_apis
urlpatterns = [
   path('vendors/',vendor_apis.VendorsList.as_view()),
   path('vendors/<str:pk>/',vendor_apis.VendorsDetail.as_view())
]