from django.urls import path
from app .views import home_view, shop_view, shop_detail_view, products_view, product_detail_view
from users .views import cart_view, xaridlar_view, users_view, xatolik_view
from contact .views import contact_view
urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop_detail/', shop_detail_view, name='shop_detail'),
    path('cart/', cart_view, name='cart'),
    path('xaridlar/', xaridlar_view, name='xaridlar'),
    path('users/', users_view, name='users'),
    path('xatolik/', xatolik_view, name='xatolik'),
    path('contact/', contact_view, name='contact'),
    path('product/', products_view, name='products'),
    path('products/<slug:slug>/', product_detail_view, name='product-detail'),
]
