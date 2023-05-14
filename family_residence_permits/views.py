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
from .models import Explanation, Document, Visit_place, Family_residence_permit
from .serializers import ExplanationSerializer, DocumentSerializer, Visit_placeSerializer, Family_residence_permitDetailSerializer, Family_residence_permitListSerializer

class Explanations(APIView):
    def get(self, request):
        all_explanations = Explanation.objects.all()
        serializer = ExplanationSerializer(all_explanations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExplanationSerializer(data=request.data)
        if serializer.is_valid():
           explanation = serializer.save()
           return Response(ExplanationSerializer(explanation).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ExplanationDetail(APIView):
    def get_object(self, pk):
        try: 
            return Explanation.objects.get(pk=pk)
        except Explanation.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        explanation = self.get_object(pk)
        serializer = ExplanationSerializer(explanation)
        return Response(serializer.data)

    def put(self, request, pk):
        explanation = self.get_object(pk)
        serializer = ExplanationSerializer(explanation, data=request.data, partial=True)
        if serializer.is_valid():
            updated_explanation = serializer.save()
            return Response(ExplanationSerializer(updated_explanation).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        explanation = self.get_object(pk)
        explanation.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Documents(APIView):
    def get(self, request):
        all_documents = Document.objects.all()
        serializer = DocumentSerializer(all_documents, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
           document = serializer.save()
           return Response(DocumentSerializer(document).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class DocumentDetail(APIView):
    def get_object(self, pk):
        try: 
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document, data=request.data, partial=True)
        if serializer.is_valid():
            updated_document = serializer.save()
            return Response(DocumentSerializer(updated_document).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        document = self.get_object(pk)
        document.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Visit_places(APIView):
    def get(self, request):
        all_visit_places = Visit_place.objects.all()
        serializer = Visit_placeSerializer(all_visit_places, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Visit_placeSerializer(data=request.data)
        if serializer.is_valid():
           visit_place = serializer.save()
           return Response(Visit_placeSerializer(visit_place).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Visit_placeDetail(APIView):
    def get_object(self, pk):
        try: 
            return Visit_place.objects.get(pk=pk)
        except Visit_place.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        visit_place = self.get_object(pk)
        serializer = Visit_placeSerializer(visit_place)
        return Response(serializer.data)

    def put(self, request, pk):
        visit_place = self.get_object(pk)
        serializer = Visit_placeSerializer(visit_place, data=request.data, partial=True)
        if serializer.is_valid():
            updated_visit_place = serializer.save()
            return Response(Visit_placeSerializer(updated_visit_place).data,)
        else:
          return Response(serializer.error)  

    def delete(self, request, pk):
        visit_place = self.get_object(pk)
        visit_place.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Family_residence_permits(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_family_residence_permits = Family_residence_permit.objects.all()
        serializer = Family_residence_permitListSerializer(all_family_residence_permits, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Family_residence_permitDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    family_residence_permit = serializer.save(expat = request.user)
                    explanations = request.data.get("explanations")
                    for explanation_pk in explanations:
                        explanation = Explanation.objects.get(pk=explanation_pk)
                        family_residence_permit.explanations.add(explanation)
                    documents = request.data.get("documents")
                    for document_pk in documents:
                        document = Document.objects.get(pk=document_pk)
                        family_residence_permit.documents.add(document)    
                    serializer = Family_residence_permitDetailSerializer(family_residence_permit, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Explanation.DoesNotExist):
                    raise ParseError("Explanation not found")
                elif isinstance(e, Document.DoesNotExist):
                    raise ParseError("Document not found") 
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Family_residence_permitDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Family_residence_permit.objects.get(pk=pk)
        except Family_residence_permit.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        family_residence_permit = self.get_object(pk)
        serializer = Family_residence_permitDetailSerializer(family_residence_permit, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        family_residence_permit = self.get_object(pk)
        if not family_residence_permit.expat == request.user or not request.user.is_supporter and not request.user.is_family_residence_permits:
            raise PermissionDenied

    def delete(self, request, pk):
        family_residence_permit = self.get_object(pk)
        if not family_residence_permit.expat == request.user or not request.user.is_supporter and not request.user.is_family_residence_permits:
            raise PermissionDenied
        family_residence_permit.delete()
        return Response(status=HTTP_204_NO_CONTENT)