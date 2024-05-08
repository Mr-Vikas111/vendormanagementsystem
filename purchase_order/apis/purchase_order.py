
from django.shortcuts import render 
from django.http import Http404 
  
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated, AllowAny


from purchase_order.serializers import purchase_order as po_serializers
from purchase_order.utils import po as po_utils
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

status200 = status.HTTP_200_OK
status201 = status.HTTP_201_CREATED
status202 = status.HTTP_202_ACCEPTED
status204 = status.HTTP_204_NO_CONTENT
status400 = status.HTTP_400_BAD_REQUEST
status401 = status.HTTP_401_UNAUTHORIZED
status404 = status.HTTP_404_NOT_FOUND


class POList(APIView): 
    """ 
    List all Transformers, or create a new Transformer 
    """
    

    permission_classes = [IsAuthenticated]


    vendor_id = openapi.Parameter('vendor', openapi.IN_QUERY,
                          description="Vender ID",
                          type=openapi.TYPE_STRING, required=False)
    
    @swagger_auto_schema(manual_parameters =[vendor_id])
    def get(self, request, format=None): 
        vendor  = request.GET.get('vendor',None)
        if vendor:
            queryset = po_utils.POFunctions.all_po().filter(vendor__id=vendor)
        else:
            queryset = po_utils.POFunctions.all_po()
        serializer =po_serializers.POListSerializer(queryset, many=True) 
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK) 
    


    @swagger_auto_schema(request_body=po_serializers.POCreateSerializers, responses={200: 'OK',
                                    400: 'Bad Request'})
    def post(self, request, format=None): 
        serializer = po_serializers.POCreateSerializers(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status':True,'data':serializer.data},
                            status=status.HTTP_201_CREATED) 
        return Response({'status':False,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    

class PODetail(APIView): 
    
    def get_object(self, pk): 
        try: 
            return po_utils.POFunctions.get_po(pk)
        except:
            raise Http404 
  
    def get(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        serializer = po_serializers.PODetailSerializer(vendor) 
        return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK) 
  
    
    @swagger_auto_schema(request_body=po_serializers.PODetailSerializer, responses={200: 'OK',
                                    400: 'Bad Request'})
    def put(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        serializer = po_serializers.PODetailSerializer(vendor, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response({'status':False,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        
  
    def delete(self, request, pk, format=None): 
        vendor = self.get_object(pk) 
        vendor.delete() 
        return Response({'status':True,'msg':'Data Deleted'},status=status.HTTP_200_OK)