# Generated by Django 5.0.3 on 2024-04-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0008_remove_food_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]