
from rest_framework.routers import DefaultRouter
from .views import  CategoryViewSet, FoodViewSet, ReviewViewSet

from django.urls import path, include



router = DefaultRouter()
router.register('food', FoodViewSet)
router.register('review', ReviewViewSet)
router.register('category', CategoryViewSet)





urlpatterns = [
    path('', include(router.urls)),
]


