from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import UserDataSerializer
from ..models import UserData


class UserDataViewSet(ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UserDataView(RetrieveAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UserDataView(CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UpdateUserData(UpdateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer