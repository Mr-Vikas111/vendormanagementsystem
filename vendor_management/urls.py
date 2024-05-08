from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include


schema_view = get_schema_view(
   openapi.Info(
      title="Vendor API",
      default_version='v1',
      description="Vendors API Doc",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path('admin/', admin.site.urls),
      # plugins URLS
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swagger URL
    path('api/',include('vendor.urls')),
    path('api/',include('purchase_order.urls')),
    path('auth/',include('user.urls'))
]
