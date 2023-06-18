import time
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Company_cars_supporter
from .serializers import Company_cars_supporterDetailSerializer, Company_cars_supporterListSerializer

class Company_cars_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_company_cars_supporters = Company_cars_supporter.objects.all()
        serializer = Company_cars_supporterListSerializer(all_company_cars_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Company_cars_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    company_cars_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Company_cars_supporterDetailSerializer(company_cars_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Company_cars_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Company_cars_supporter.objects.get(pk=pk)
        except Company_cars_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        company_cars_supporter = self.get_object(pk)
        serializer = Company_cars_supporterDetailSerializer(company_cars_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        company_cars_supporter = self.get_object(pk)
        if company_cars_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        company_cars_supporter = self.get_object(pk)
        if company_cars_supporter.responsible_person != request.user:
            raise PermissionDenied
        company_cars_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)