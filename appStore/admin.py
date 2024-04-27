from django.contrib import admin

from .models import  Category,Food, Review


class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('category_name',)}

        list_display = ['slug', 'category_name']



class FoodAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('food_name',)}
        list_display = ['slug', 'price', 'is_available']



admin.site.register(Food, FoodAdmin)
admin.site.register(Review)
admin.site.register(Category, CategoryAdmin)





