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
from .models import Company_car
from .serializers import Company_carDetailSerializer, Company_carListSerializer

class Company_cars(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_company_cars = Company_car.objects.all()
        serializer = Company_carListSerializer(all_company_cars, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Company_carDetailSerializer(data=request.data)
        if serializer.is_valid():
                    company_car = serializer.save(responsible_person = request.user)   
                    serializer = Company_carDetailSerializer(company_car, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Company_carDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Company_car.objects.get(pk=pk)
        except Company_car.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        company_car = self.get_object(pk)
        serializer = Company_carDetailSerializer(company_car, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        company_car = self.get_object(pk)
        if company_car.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        company_car = self.get_object(pk)
        if company_car.responsible_person != request.user:
            raise PermissionDenied
        company_car.delete()
        return Response(status=HTTP_204_NO_CONTENT)