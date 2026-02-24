from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # OnlineOrder
    path('online_orders/', views.online_orders_list, name='online_orders_list'),
    path('online_orders/add/', views.online_order_add, name='online_order_add'),
    path('online_orders/<uuid:pk>/edit/', views.online_order_edit, name='online_order_edit'),
    path('online_orders/<uuid:pk>/delete/', views.online_order_delete, name='online_order_delete'),
    path('online_orders/bulk/', views.online_orders_bulk_action, name='online_orders_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
