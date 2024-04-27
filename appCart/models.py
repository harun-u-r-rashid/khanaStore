from django.db import models
from appStore.models import Food
from django.contrib.auth.models import User



class Cart(models.Model):
        id = models.IntegerField(primary_key=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank= True)
        food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True, related_name='cartitems')
        quantity = models.IntegerField(default=1)
        date_added = models.DateTimeField(auto_now_add = True)

        def __str__(self):
                return f"{self.id}"
        


        
    



    




