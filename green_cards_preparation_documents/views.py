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
from .models import Green_cards_preparation_document
from .serializers import Green_cards_preparation_documentDetailSerializer, Green_cards_preparation_documentListSerializer

class Green_cards_preparation_documents(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_green_cards_preparation_documents = Green_cards_preparation_document.objects.all()
        serializer = Green_cards_preparation_documentListSerializer(all_green_cards_preparation_documents, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Green_cards_preparation_documentDetailSerializer(data=request.data)
        if request.user.is_supporter and request.user.is_green_cards and serializer.is_valid():
            green_cards_preparation_document = serializer.save(expat = request.user)
            serializer = Green_cards_preparation_documentDetailSerializer(green_cards_preparation_document, context={"request": request},)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Green_cards_preparation_documentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Green_cards_preparation_document.objects.get(pk=pk)
        except Green_cards_preparation_document.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        green_cards_preparation_document = self.get_object(pk)
        serializer = Green_cards_preparation_documentDetailSerializer(green_cards_preparation_document, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        green_cards_preparation_document = self.get_object(pk)
        serializer = Green_cards_preparation_documentDetailSerializer(green_cards_preparation_document, data=request.data, partial=True)
        if request.user.is_supporter and request.user.is_green_cards and serializer.is_valid():
            updated_green_cards_preparation_document = serializer.save()
            return Response(Green_cards_preparation_documentDetailSerializer(updated_green_cards_preparation_document).data,)
        else:
          raise PermissionDenied

    def delete(self, request, pk):
        green_cards_preparation_document = self.get_object(pk)
        if not request.user.is_supporter and request.user.is_green_cards:
            raise PermissionDenied
        green_cards_preparation_document.delete()
        return Response(status=HTTP_204_NO_CONTENT)