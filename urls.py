from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('settings/', views.settings, name='settings'),
]
