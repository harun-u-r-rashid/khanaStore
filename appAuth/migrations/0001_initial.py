# Generated by Django 5.0.3 on 2024-04-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
