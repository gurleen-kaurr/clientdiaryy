# Generated by Django 2.2.28 on 2024-12-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_details', '0004_auto_20240728_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_phno',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]