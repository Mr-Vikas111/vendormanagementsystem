from django.urls import path
from purchase_order.apis import purchase_order as po_apis

urlpatterns = [
   path('purchase_orders/',po_apis.POList.as_view()),
   path('purchase_orders/<str:pk>/',po_apis.PODetail.as_view()),
]