from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegistrationApiView, activate, LoginApiView, LogoutAPIView, ContactView


router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
        path("", include(router.urls)),
        path('register/', RegistrationApiView.as_view(), name='register'),
        path('active/<uidb64>/<token>/', activate, name='active'),
        path('login/', LoginApiView.as_view(), name = 'login'),
        path('logout/', LogoutAPIView.as_view(), name='logout'),
        path('contact/', ContactView.as_view(), name='contact')
        
      
]