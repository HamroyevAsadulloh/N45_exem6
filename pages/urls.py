from django.urls import path
from .views import client_view

urlpatterns = [
    path('Clients/', client_view, name='Clients'),
]
