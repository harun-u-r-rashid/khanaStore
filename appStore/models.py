from django.db import models
from .constants import STAR
from django.contrib.auth.models import User




class Category(models.Model):
        category_name = models.CharField(max_length = 40, unique = True)
        slug = models.SlugField(max_length = 50)
        description = models.TextField(max_length = 200, blank = True)
        category_image = models.ImageField(upload_to='photos/category')

        def __str__(self):
                return f"{self.category_name}"
        



class Food(models.Model):
        category = models.ForeignKey(Category, on_delete = models.CASCADE)
        food_name = models.CharField(max_length = 20, unique=True)
        food_image = models.ImageField(upload_to='photos/food')
        description = models.TextField(max_length=150, null=True, blank=True)
        slug = models.SlugField(max_length = 30)
        price = models.IntegerField()
        is_available = models.BooleanField(default = True)
        created_date = models.DateTimeField(auto_now_add = True)

        def _str__(self):
                return f"{self.food_name}"





class Review(models.Model):
        user = models.ForeignKey(User, on_delete = models.CASCADE)
        food = models.ForeignKey(Food, on_delete = models.CASCADE)
        review = models.TextField(max_length = 100)
        rating = models.CharField(max_length=6, choices = STAR)
        review_date = models.DateTimeField(auto_now_add = True)

        def __str__(self):
                return f"{self.user.username} reviewed to {self.food.food_name}"
        


