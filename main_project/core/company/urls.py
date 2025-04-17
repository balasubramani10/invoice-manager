

from django.urls import path, include
from .views import dashboard
from . import views as app_views  # replace with your actual app name



urlpatterns = [
   
 
    path("",dashboard, name="dashboard"),
    path('login/', app_views.login_view, name='login'),
    path('logout/', app_views.logout_view, name='logout'),



]
