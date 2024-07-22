from django.urls import path
from .views import cart_view, xaridlar_view, users_view, xatolik_view, login_view, register_view, logout_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('xaridlar/', xaridlar_view, name='xaridlar'),
    path('users/', users_view, name='users'),
    path('xatolik/', xatolik_view, name='xatolik'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
