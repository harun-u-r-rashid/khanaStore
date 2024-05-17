from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.CartViewSet)


urlpatterns = [  
    path('', include(router.urls)),
    # path('update/<int:cart_id>/', views.UpdateCartQuantityView.as_view(), name='updateQuantity'),
    path('delete/<int:cart_id>/', views.DeleteCartView.as_view(), name='delete'),
 
]


