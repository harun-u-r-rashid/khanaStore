from django.shortcuts import render,get_object_or_404
from .models import Cart
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CartSerializer, CartQuantityUpdateSerializer, CartDeleteSerializer
from appStore.models import Food



class CartViewSet(viewsets.ModelViewSet):
        queryset = Cart.objects.all()
        serializer_class = CartSerializer

        def get_queryset(self):
            queryset = super().get_queryset()  
            user_id = self.request.query_params.get('user_id')
            if user_id:
                   queryset = queryset.filter(user_id=user_id)

            return queryset
        

        def create(self, request, *args, **kwargs):
            user_id = request.data.get('user')
            food_id = request.data.get('food')
            user = User.objects.get(id=user_id)
            food = Food.objects.get(id=food_id)
            quantity = int(request.data.get('quantity', 1))
            
            cart_item = Cart.objects.create(
                user=user,
                food=food,
                quantity=quantity
            )

            serializer = self.get_serializer(cart_item)
            return Response(serializer.data)




# class UpdateCartQuantityView(generics.GenericAPIView):
#       serializer_class = CartQuantityUpdateSerializer

#       def put(self, request, cart_id):
#             cart = get_object_or_404(Cart, pk=cart_id)
#             serializer = self.serializer_class(instance=cart, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_200_OK, data=serializer.data)
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
      


class DeleteCartView(generics.GenericAPIView):
      serializer_class = CartDeleteSerializer
      def delete(self, request, cart_id):
            cart = Cart.objects.get(pk = cart_id)
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      




        
                
        
                          
