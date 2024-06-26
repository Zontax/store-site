# Generated by Django 4.2.11 on 2024-03-18 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL Slug')),
            ],
            options={
                'verbose_name': 'Категорію',
                'verbose_name_plural': 'Категорії',
                'db_table': 'goods_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL Slug')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Зображення')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Ціна')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Знижка')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
                'db_table': 'goods_products',
            },
        ),
    ]
