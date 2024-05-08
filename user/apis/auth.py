from rest_framework.response import Response
from rest_framework import permissions, generics, status, views
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from rest_framework import status

# swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# JWT imports
from rest_framework.permissions import IsAuthenticated, AllowAny

# application imports
from user.serializers import base as user_base_serializers
from helper import keys
from user.utils import base as base_user_utils


status200 = status.HTTP_200_OK
status201 = status.HTTP_201_CREATED
status202 = status.HTTP_202_ACCEPTED
status204 = status.HTTP_204_NO_CONTENT
status400 = status.HTTP_400_BAD_REQUEST
status401 = status.HTTP_401_UNAUTHORIZED
status404 = status.HTTP_404_NOT_FOUND


class LoginAPI(generics.CreateAPIView):
    """ 
    API to add new lead information
    
    HEAD PARAM: JWT Token
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Empty String 

    """
    serializer_class = user_base_serializers.UserLoginSerializer
    
    def create(self, request, *args, **kwargs):
        login_serializer = user_base_serializers.UserLoginSerializer(data=request.data)
        if not login_serializer.is_valid(raise_exception=False):
            errors = login_serializer.errors
            return Response({'status':False,'msg':str(errors)}, status=status400)
        else:
            data = login_serializer.data
            data[keys.EMAIL] = base_user_utils.UserFunctions.remove_space(data[keys.EMAIL])
            data[keys.PASSWORD] =  base_user_utils.UserFunctions.remove_space(data[keys.PASSWORD])
            res =  base_user_utils.UserFunctions.validate_user(**{keys.EMAIL:data[keys.EMAIL] ,keys.PASSWORD: data[keys.PASSWORD]})
            try:
                if not res[keys.STATUS]:
                    return Response({'status':False,'msg':res[keys.MESSAGE]},status=status400)
                else:
                    return Response({keys.ACCESS_TOKEN: res[keys.RESPONSE][keys.ACCESS], keys.REFRESH_TOKEN: res[keys.RESPONSE][keys.REFRESH]})
            except Exception as e:
                return Response({'status':False,'msg':str(e)},status=status400)