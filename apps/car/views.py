from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import CarModel
from apps.car.serializers import CarSerializer


class CarCreateListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        params = self.request.query_params
        user_id = params.get('userId', None)
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs


class RetrieveDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
