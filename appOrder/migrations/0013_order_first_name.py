# Generated by Django 5.0.3 on 2024-05-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOrder', '0012_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
