from .models import Category ,Food, Review
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
                model = Category
                fields = '__all__'




class FoodSerializer(serializers.ModelSerializer):
        class Meta:
                model = Food
                fields = '__all__'
                

class ReviewSerializer(serializers.ModelSerializer):
        user = serializers.StringRelatedField(many=False)
        food = serializers.StringRelatedField(many=False)
        class Meta:
                model = Review
                fields = '__all__'


class AddReviewSerializer(serializers.ModelSerializer):
        class Meta:
                model = Review
                fields = '__all__'

                

