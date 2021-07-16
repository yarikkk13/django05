from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import CarModel
from apps.car.serializers import CarSerializer


class CarCreateListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel


class RetrieveDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel
