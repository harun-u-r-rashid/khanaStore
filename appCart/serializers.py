from rest_framework import serializers
from appStore.models import Food
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    food_name = serializers.CharField(source='food.food_name')

    class Meta:
        model = Cart
        fields = '__all__'



class CartQuantityUpdateSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = Cart
        fields = ['quantity']




class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

