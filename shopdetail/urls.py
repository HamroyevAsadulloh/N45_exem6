from django.urls import path
from .views import shop_detail_view

urlpatterns = [
    path('shop_detail/', shop_detail_view, name='shop-detail'),
]
