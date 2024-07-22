from django.urls import path
from .views import shop_view


urlpatterns = [
    path('shop/', shop_view, name='shop'),
]
