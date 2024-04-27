# from django.db import models
# from .constants import PAYMNENT_STATUS
# from django.contrib.auth.models import User
# from appStore.models import Food




# class Order(models.Model):
#         user = models.ForeignKey(User, on_delete=models.CASCADE)
#         orderDate = models.DateTimeField(auto_now_add = True)
#         status = models.CharField(max_length=30, choices = PAYMNENT_STATUS, default='PENDING')

#         def __str__(self):
#                 return f"{self.user.username} X {self.status}"
        



# class OrderItem(models.Model):
#         order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='items')
#         food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)

#         quantity  = models.IntegerField(default=0)


#         def __str__(self):
#                 return f"{self.food.food_name}"



from .constants import ORDER_STATUS
from django.db import models
from django.contrib.auth.models import User
from appStore.models import Food



class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length= 100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.IntegerField()
    status = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
        food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
        first_name = models.CharField(max_length=100, null=True, blank=True)
        last_name = models.CharField(max_length=100, null=True, blank=True)
        phone = models.CharField(max_length=12, null=True, blank=True)
        email = models.EmailField(max_length=50, null=True, blank=True)
        address_line1 = models.CharField(max_length=100, null=True, blank=True)
        address_line2 = models.CharField(max_length=100, null=True, blank=True)
        country = models.CharField(max_length=100, null=True, blank=True)
        state = models.CharField(max_length=100, null=True, blank=True)
        city = models.CharField(max_length=100, null=True, blank=True)
        quantity = models.IntegerField(default=1)
        payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
        status = models.CharField(max_length=30, choices = ORDER_STATUS, default='PENDING')
        orderDate = models.DateTimeField(auto_now_add = True)

        def __str__(self):
                return f"{self.user.username}"
        


