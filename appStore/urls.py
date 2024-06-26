
from rest_framework.routers import DefaultRouter
from .views import  CategoryViewSet, FoodViewSet,ReviewViewSet, ReviewAdd, ReviewList

from django.urls import path, include

router = DefaultRouter()
router.register('food', FoodViewSet)
router.register('reviews', ReviewViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/review/', ReviewList.as_view(), name="foodReview"),
    path('reviewAdd/<int:pk>/', ReviewAdd.as_view(), name='addReview'), 
]


