from django.urls import path
from . import views


urlpatterns = [
    path('',views.CartView.as_view(),name='carts'), 
    path('update_cart/<int:cart_id>/',views.UpdateCartView.as_view(),name='update_cart'),
]

