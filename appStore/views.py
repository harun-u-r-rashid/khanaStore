from django.shortcuts import render
from .models import  Category, Food, Review
from .serializers import  CategorySerializer, FoodSerializer, ReviewSerializer
from rest_framework import filters, pagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication

class FoodViewSet(viewsets.ModelViewSet):
        queryset = Food.objects.all()
        serializer_class = FoodSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['slug', 'category__category_name','food_name']
        




class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer



class ReviewViewSet(viewsets.ModelViewSet):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer




class ReviewList(generics.ListAPIView):
        serializer_class = ReviewSerializer
        def get_queryset(self):
                pk = self.kwargs['pk']
                return Review.objects.filter(food=pk)
        


class ReviewAdd(generics.CreateAPIView):
        serializer_class = ReviewSerializer
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]

        def get_queryset(self):
                return Review.objects.all()
        
        def perform_create(self, serializer):
                pk = self.kwargs.get('pk')
                print(pk)
                
                review = Food.objects.get(pk = pk)
                user = self.request.user
                reviewExist = Review.objects.filter(user = user, food = review)

                if reviewExist.exists():
                        raise ValidationError("You already added the review")
                review.save()
                serializer.save(food=review, user=user)


