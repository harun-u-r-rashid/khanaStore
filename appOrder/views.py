from django.shortcuts import render,get_object_or_404
from .models import Order
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import OrderSerailizer, OrderDeleteSerializer
from appStore.models import Food




class OrderViewSet(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerailizer
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
            first_name=request.data.get("first_name")
            
            order_item = Order.objects.create(
                user=user,
                food=food,
                quantity=quantity,
                first_name = first_name
            )

            serializer = self.get_serializer(order_item)
            return Response(serializer.data)



class DeleteOrderView(generics.GenericAPIView):
      serializer_class = OrderDeleteSerializer
      def delete(self, request, order_id):
            order = Order.objects.get(pk = order_id)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      