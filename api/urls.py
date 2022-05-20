from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.api_home)
]