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
from .models import Available_country, Green_cards_request
from .serializers import Available_countrySerializer, Green_cards_requestDetailSerializer, Green_cards_requestListSerializer

class Available_countries(APIView):
    def get(self, request):
        all_available_countries = Available_country.objects.all()
        serializer = Available_countrySerializer(all_available_countries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Available_countrySerializer(data=request.data)
        if serializer.is_valid():
           available_country = serializer.save()
           return Response(Available_countrySerializer(available_country).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Available_countryDetail(APIView):
    def get_object(self, pk):
        try: 
            return Available_country.objects.get(pk=pk)
        except Available_country.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        available_country = self.get_object(pk)
        serializer = Available_countrySerializer(available_country)
        return Response(serializer.data)

    def put(self, request, pk):
        available_country = self.get_object(pk)
        serializer = Available_countrySerializer(available_country, data=request.data, partial=True)
        if serializer.is_valid():
            updated_available_country = serializer.save()
            return Response(Available_countrySerializer(updated_available_country).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        available_country = self.get_object(pk)
        available_country.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Green_cards_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_green_cards_requests = Green_cards_request.objects.all()
        serializer = Green_cards_requestListSerializer(all_green_cards_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Green_cards_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    green_cards_request = serializer.save(expat = request.user)
                    available_countries = request.data.get("available_countries")
                    for available_country_pk in available_countries:
                        available_country = Available_country.objects.get(pk=available_country_pk)
                        green_cards_request.available_countries.add(available_country) 
                    serializer = Green_cards_requestDetailSerializer(green_cards_request, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Available_country.DoesNotExist):
                    raise ParseError("Explanation not found")

        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Green_cards_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Green_cards_request.objects.get(pk=pk)
        except Green_cards_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        green_cards_request = self.get_object(pk)
        serializer = Green_cards_requestDetailSerializer(green_cards_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        green_cards_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_green_cards or green_cards_request.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        green_cards_request = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_green_cards or green_cards_request.expat != request.user:
            raise PermissionDenied
        green_cards_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)