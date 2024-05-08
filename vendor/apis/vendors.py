
from django.shortcuts import render 
from django.http import Http404 
  
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated, AllowAny


from vendor.serializers import vendors as vendors_serializers
from vendor.utils import vendor as vendor_utils
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class VendorsList(APIView): 
    """ 
    List all Transformers, or create a new Transformer 
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None): 
        queryset = vendor_utils.VendorFunctions.all_vendors()
        serializer =vendors_serializers.VendorsListSerializer(queryset, many=True) 
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK) 
    


    @swagger_auto_schema(request_body=vendors_serializers.VendorsCreateSerializers, responses={200: 'OK',
                                    400: 'Bad Request'})
    def post(self, request, format=None): 
        serializer = vendors_serializers.VendorsCreateSerializers(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED) 
        return Response({'status':False,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    

class VendorsDetail(APIView): 
    
    def get_object(self, pk): 
        try: 
            return vendor_utils.VendorFunctions.get_vendor(pk)
        except:
            raise Http404 
  
    def get(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        serializer = vendors_serializers.VendorsDetailSerializer(vendor) 
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK) 
  
    
    @swagger_auto_schema(request_body=vendors_serializers.VendorsDetailSerializer, responses={200: 'OK',
                                    400: 'Bad Request'})
    def put(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        serializer = vendors_serializers.VendorsDetailSerializer(vendor, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
  
    def delete(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        vendor.delete() 
        return Response({'status':True,'msg':'Data Deleted'},status=status.HTTP_200_OK)