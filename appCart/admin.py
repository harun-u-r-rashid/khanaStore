from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
        list_display = ['id', 'user', 'get_food_slug', 'food']

        def get_food_slug(self, obj):
                return obj.food.slug if obj.food else None
        get_food_slug.short_description = ''


admin.site.register(Cart, CartAdmin)