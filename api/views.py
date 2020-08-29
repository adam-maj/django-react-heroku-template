from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import ExampleModel
# from .serializers import ExampleModelSerializer

# =========================== EXAMPLE API ENDPOINTS ===========================

# class APIOverview(APIView):
#     api_urls = {
#         'Example Model List': 'example-model-list/',
#         'Example Model Detail': 'example-model-detail/<int:pk>' 
#     }

#     def get(self, request, format=None):
#         return Response(self.api_urls, status=status.HTTP_200_OK)

# class ExampleModelList(APIView):
#     def get(self, request, format=None):
#         example_model_list = ExampleModel.objects.all()
#         serializer = ExampleModelSerializer(example_model_list, many=True)
#         return Response(serializer.data status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         new_example_model = request.data
#         serializer = ExampleModelSerializer(data=new_example_model)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# class ExampleModelDetail(APIView):
#     def put(self, request, pk, format=None):
#         example_model = ExampleModel.objects.get(id=pk)
#         updated_example_model = request.data
#         serializer = ExampleModelSerializer(example_model, data=updated_example_model)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         example_model = ExampleModel.objects.get(id=pk)
#         example_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)