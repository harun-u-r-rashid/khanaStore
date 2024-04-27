from django.shortcuts import render,get_object_or_404
from .models import Order
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User



class OrderView(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user = request.user
        if  user.is_superuser:
            orders=Order.objects.all()
            serializer=self.serializer_class(instance=orders,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            orders=Order.objects.filter(user=user)
            serializer=self.serializer_class(instance=orders,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)

  
   







class UpdateOrderView(generics.GenericAPIView):
    
    serializer_class=serializers.OrderUpdateSerializer
    permission_classes=[IsAuthenticated]

 
    def put(self, request,order_id):
        order=get_object_or_404(Order,pk=order_id)

        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK,data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)





class UpdateOrderStatusView(generics.GenericAPIView):
    
    serializer_class=serializers.OrderStatusUpdateSerializer
    permission_classes=[IsAdminUser]

 
    def put(self, request,order_id):
        order=get_object_or_404(Order,pk=order_id)

        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK,data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)






class UserOrdersView(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)

        orders=Order.objects.all().filter(user=user)

        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)












