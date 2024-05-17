from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
        list_display = ['user', 'get_food_slug']
        def get_food_slug(self, obj):
                return obj.food.slug if obj.food else None
        get_food_slug.short_description = 'slug'

admin.site.register(Order, OrderAdmin)
