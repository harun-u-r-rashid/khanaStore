from django.shortcuts import render,get_object_or_404
from .models import Cart
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User





class CartView(generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class=serializers.CartSerializer
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user = request.user
        if  user.is_superuser:
            carts=Cart.objects.all()
            serializer=self.serializer_class(instance=carts,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            carts=Cart.objects.filter(user=user)
            serializer=self.serializer_class(instance=carts,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
                 


class UpdateCartView(generics.GenericAPIView):
        serializer_class=serializers.CartUpdateSerializer
        permission_classes=[IsAuthenticated]

        def put(self, request,cart_id):
                cart=get_object_or_404(Cart, pk=cart_id)
                serializer=self.serializer_class(instance=cart,data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(status=status.HTTP_200_OK,data=serializer.data)
                        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)
