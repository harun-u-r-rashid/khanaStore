# Generated by Django 5.0.3 on 2024-04-26 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0003_food_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='in_stock',
        ),
    ]
