from django.urls import path
from . import views

urlpatterns = [
  path('user', views.getData),
  path('login', views.getData),
]