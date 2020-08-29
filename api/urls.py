from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('', views.APIOverview.as_view()),
    # path('example-model-list/', views.ExampleModelList.as_view()),
    # path('example-model-detail/<int:pk>', views.ExampleModelDetail.as_view()),
]