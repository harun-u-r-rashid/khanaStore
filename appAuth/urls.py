from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationApiView, activate, LoginApiView, LogoutAPIView, ContactView

urlpatterns = [

        path('register/', RegistrationApiView.as_view(), name='register'),
        path('active/<uidb64>/<token>/', activate, name='active'),
        path('login/', LoginApiView.as_view(), name = 'login'),
        path('logout/', LogoutAPIView.as_view(), name='logout'),
        path('contact/', ContactView.as_view(), name='contact')
        
      
]