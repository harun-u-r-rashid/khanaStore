from django.shortcuts import render
from .models import  Category, Food, Review
from .serializers import  CategorySerializer, FoodSerializer, ReviewSerializer
from rest_framework import filters, pagination
from rest_framework import viewsets




class FoodViewSet(viewsets.ModelViewSet):
        queryset = Food.objects.all()
        serializer_class = FoodSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['slug', 'category__category_name','food_name']
        


class ReviewViewSet(viewsets.ModelViewSet):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer







