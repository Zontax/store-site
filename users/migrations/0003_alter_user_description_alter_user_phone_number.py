# Generated by Django 4.2.11 on 2024-03-22 10:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_description_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Опис профілю'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='UA', verbose_name='Номер телефону'),
        ),
    ]
