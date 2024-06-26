# Generated by Django 4.2.11 on 2024-03-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAdvertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('description', models.TextField(max_length=1000, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisement_images', verbose_name='Зображення')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')),
                ('disable_timestamp', models.DateTimeField(verbose_name='Коли вимкнути')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активне')),
            ],
            options={
                'verbose_name': 'Оголошення',
                'db_table': 'advertisements',
                'ordering': ('-created_timestamp',),
            },
        ),
    ]
