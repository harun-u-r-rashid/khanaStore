# Generated by Django 5.0.3 on 2024-05-17 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOrder', '0013_order_first_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]