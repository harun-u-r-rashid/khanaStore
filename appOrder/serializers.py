# from .models import Order, OrderItem
# from rest_framework import serializers
# from appStore.models import Food
# from django.db import transaction
# from appCart.models import Cart, CartItem
# class SimpleProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Food
#         fields = ["id","food_name", "price"]
        


# class OrderItemSerailizer(serializers.ModelSerializer):
#         food = SimpleProductSerializer()
#         class Meta:
#                 model = OrderItem
#                 fields = ['id', 'food', 'quantity']



# class OrderSerializer(serializers.ModelSerializer):
#         items = OrderItemSerailizer(many = True, read_only = True)
#         class Meta:
#                 model = Order
#                 fields = ['id', 'user', 'orderDate', 'status', 'items']




# class CreateOrderSerializer(serializers.Serializer):
#     cart_id = serializers.UUIDField()
    
    
    
#     def validate_cart_id(self, cart_id):
#         if not Cart.objects.filter(pk=cart_id).exists():
#             raise serializers.ValidationError("This cart_id is invalid")
        
#         elif not CartItem.objects.filter(cart_id=cart_id).exists():
#             raise serializers.ValidationError("Sorry your cart is empty")
        
#         return cart_id
    
    
    
#     def save(self, **kwargs):
#         with transaction.atomic():
#             cart_id = self.validated_data["cart_id"]
#             user_id = self.context["user_id"]
#             order = Order.objects.create(user_id = user_id)
#             cartitems = CartItem.objects.filter(cart_id=cart_id)
#             orderitems = [
#                 OrderItem(order=order, 
#                     food=item.food, 
#                     quantity=item.quantity
#                     )
#             for item in cartitems
#             ]
#             OrderItem.objects.bulk_create(orderitems)
            
#             return order


# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order 
#         fields = ["status"]


from .models import Order
from rest_framework import serializers



class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    food_name = serializers.CharField(source='food.food_name')
    
    class Meta:
        model = Order
        fields = ['user', 'food_name', 'status', 'quantity']

        


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
        status = serializers.CharField(max_length = 30)
        class Meta:
                model = Order
                fields = ['status']





class OrderUpdateSerializer(serializers.ModelSerializer):
       
        class Meta:
                model = Order
                fields = ['first_name', 'last_name', 'phone', 'email', 'state', 'city', 'country', 'quantity']

