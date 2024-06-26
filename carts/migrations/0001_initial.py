# Generated by Django 4.2.11 on 2024-03-19 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True, verbose_name='Не зареєстрований (ключ сесії)')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product', verbose_name='Товар')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Власник корзини')),
            ],
            options={
                'verbose_name': 'Кошик',
                'verbose_name_plural': 'Кошик',
                'db_table': 'carts',
            },
        ),
    ]
