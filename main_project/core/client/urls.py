

from django.urls import path, include
from .views import add_client, view_clients, edit_client, delete_client



urlpatterns = [
   
    path("add",add_client, name="add_client"),
    path("",view_clients, name="view_clients"),
    path('edit/<int:pk>/', edit_client, name='edit_client'),
    path('delete/<int:pk>/', delete_client, name='delete_client'),


]
