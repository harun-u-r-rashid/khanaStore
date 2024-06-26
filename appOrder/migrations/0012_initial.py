# Generated by Django 5.0.3 on 2024-05-16 05:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appOrder', '0011_remove_payment_user_delete_order_delete_payment'),
        ('appStore', '0009_food_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='appStore.food')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
