# Generated by Django 5.1.3 on 2024-12-05 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_rename_cart_cartlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
