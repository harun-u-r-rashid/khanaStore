from rest_framework import serializers
from appStore.models import Food
from .models import Cart



class SimpleFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id","food_name", "price"]
        

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    food_name = serializers.CharField(source='food.food_name')

    class Meta:
        model = Cart
        fields = ['user', 'food_name', 'quantity']



class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['food', 'quantity']
