

from django.urls import path, include
from .views import add_product, view_products, edit_product, delete_product




urlpatterns = [
   
    path("add",add_product, name="add_product"),
    path("",view_products, name="view_products"),
    path('edit/<int:pk>/', edit_product, name='edit_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),


]
