# Generated by Django 4.1.3 on 2022-12-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_price',
        ),
    ]