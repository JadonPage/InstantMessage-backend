from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

user_data_router = DefaultRouter()
user_data_router.register(r'users', UserDataViewSet)
