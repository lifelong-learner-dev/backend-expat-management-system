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
from .models import Explanation, Document, Company_cars_request
from .serializers import ExplanationSerializer, DocumentSerializer, Company_cars_requestDetailSerializer, Company_cars_requestListSerializer

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

class Company_cars_requests(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_company_cars_requests = Company_cars_request.objects.all()
        serializer = Company_cars_requestListSerializer(all_company_cars_requests, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Company_cars_requestDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    company_cars_request = serializer.save(expat = request.user)
                    explanations = request.data.get("explanations")
                    for explanation_pk in explanations:
                        explanation = Explanation.objects.get(pk=explanation_pk)
                        company_cars_request.explanations.add(explanation)
                    documents = request.data.get("documents")
                    for document_pk in documents:
                        document = Document.objects.get(pk=document_pk)
                        company_cars_request.documents.add(document) 

                    company_cars_request.krstatus = Company_cars_request.KrstatusChoices.INFORMED
                    company_cars_request.enstatus = Company_cars_request.EnstatusChoices.INFORMED
                    company_cars_request.save()

                    serializer = Company_cars_requestDetailSerializer(company_cars_request, context={"request": request},)
                    return Response(serializer.data)
            except ObjectDoesNotExist as e:
                if isinstance(e, Explanation.DoesNotExist):
                    raise ParseError("Explanation not found")
                elif isinstance(e, Document.DoesNotExist):
                    raise ParseError("Document not found") 
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Company_cars_requestDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Company_cars_request.objects.get(pk=pk)
        except Company_cars_request.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        company_cars_request = self.get_object(pk)
        serializer = Company_cars_requestDetailSerializer(company_cars_request, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        company_cars_request = self.get_object(pk)
        serializer = Company_cars_requestDetailSerializer(company_cars_request, data=request.data, partial=True)
        if request.user.is_supporter and request.user.is_company_cars and serializer.is_valid():
            updated_company_cars_request = serializer.save()
            return Response(Company_cars_requestDetailSerializer(updated_company_cars_request).data,)
        else:
          raise PermissionDenied

    def delete(self, request, pk):
        company_cars_request = self.get_object(pk)
        if company_cars_request.expat != request.user:
            raise PermissionDenied
        company_cars_request.delete()
        return Response(status=HTTP_204_NO_CONTENT)