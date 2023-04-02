from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Available_country, Green_cards_request
from .serializers import Available_countrySerializer, Green_cards_requestSerializer

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
    pass

class Green_cards_requestDetail(APIView):
    pass