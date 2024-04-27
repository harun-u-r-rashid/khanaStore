
# from django.urls import path, include
# from .views import OrderViewSet

# from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

# router = routers.DefaultRouter()

# router.register('order', OrderViewSet, basename='order')


# urlpatterns = [

#    path("", include(router.urls)),
# ] 


from django.urls import path
from . import views


urlpatterns = [
    path('',views.OrderView.as_view(),name='orders'), 
    path('update_order/<int:order_id>/',views.UpdateOrderView.as_view(),name='update_order'),
    path('update_status/<int:order_id>/',views.UpdateOrderStatusView.as_view(),name='update_status'),
    path('user/<int:user_id>/orders',views.UserOrdersView.as_view(),name='users_orders'),
  
]


