# Generated by Django 4.2.11 on 2024-03-23 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_product_meta_keywords_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
