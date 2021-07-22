from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from apps.user.serializer import UserSerializer
from apps.car.serializers import CarByUserIdSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class RetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class CreateCarByUserId(CreateAPIView):
    serializer_class = CarByUserIdSerializer
    queryset = UserModel

    def perform_create(self, serializer):
        serializer.save(user=self.get_object())
