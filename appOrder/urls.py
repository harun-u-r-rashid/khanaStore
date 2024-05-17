
from django.urls import path, include
from .views import OrderViewSet, DeleteOrderView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('', OrderViewSet, basename='order')


urlpatterns = [

   path("", include(router.urls)),
    path('delete/<int:order_id>/', DeleteOrderView.as_view(), name='delete'),
] 




