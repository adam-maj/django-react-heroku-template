from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import ExampleModel
# from .serializers import ExampleModelSerializer

class APIOverview(APIView):
    api_urls = {
        'View Name': 'View URL Slug' 
    }

    def get(self, request, format=None):
        return Response(self.api_urls, status=status.HTTP_200_OK)