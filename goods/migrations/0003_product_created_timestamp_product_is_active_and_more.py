# Generated by Django 4.2.11 on 2024-03-21 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата додавання'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Чи доступний'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='SEO ключові слова'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True, verbose_name='Код товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Знижка, %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='На складі'),
        ),
    ]