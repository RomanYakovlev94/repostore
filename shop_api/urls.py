from django.urls import path, include

from .views import *

urlpatterns = [
    path('api/v1/product/', ProductApiCreate.as_view()),
    path('api/v1/product/<int:pk>/', ProductApiUpdate.as_view()),
    path('api/v1/prod_detail/<int:pk>/', ProductApiDetailView.as_view())
]
