from django.urls import path

from .views import UserListCreateView, RetrieveUpdateDeleteView, CreateCarByUserId

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', RetrieveUpdateDeleteView.as_view(), name='user_update_delete'),
    path('/<int:pk>/cars', CreateCarByUserId.as_view(), name='create_car_by_user_id')

]
