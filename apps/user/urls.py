from django.urls import path

from .views import UserListCreateView, RetrieveUpdateDeleteView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', RetrieveUpdateDeleteView.as_view(), name='user_update_delete')

]
