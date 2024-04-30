# from django.contrib import admin

# from .models import Order, OrderItem


# class OrderAdmin(admin.ModelAdmin):
#         list_display = ['user', 'status']


# class OrderItemAdmin(admin.ModelAdmin):
#         list_display = ['order', 'food', 'quantity']


# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)



# from django.contrib import admin
# from .models import Order

# # Register your models here.



# class OrderAdmin(admin.ModelAdmin):
#     list_display=['id','foodName', 'status']
#     list_filter=['orderDate','status']

#     def foodName(self, obj):
#         return obj.food.food_name
    
   

# admin.site.register(Order, OrderAdmin)
