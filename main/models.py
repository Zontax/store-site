from django.db.models import Model, CharField, TextField, ImageField, BooleanField, DateTimeField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from traitlets import default


class BaseAdvertisement(Model):
    name = CharField('Назва', max_length=80, unique=True)
    description = CharField('Опис оголошення', max_length=300)
    css_style = TextField('CSS Стилі', max_length=600, default='', blank=True)
    image = ImageField('Зображення', upload_to='advertisement_images', blank=True, null=True)
    created_timestamp = DateTimeField('Дата додавання', auto_now_add=True)
    disable_timestamp = DateTimeField('Коли вимкнути')
    is_active = BooleanField('Активне', default=False)

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
        ordering = ('-created_timestamp',)


    def __str__(self):
        return self.name


@receiver(pre_save, sender=BaseAdvertisement)
def ensure_single_active_advertisement(sender, instance, **kwargs):
    
    if instance.pk is None:
        # Якщо це нове оголошення, переконайтеся, що всі інші оголошення встановлені в неактивний стан
        BaseAdvertisement.objects.exclude(pk=instance.pk).update(is_active=False)
    else:
        # Якщо це оновлення і активне оголошення, переконайтеся, що всі інші оголошення встановлені в неактивний стан
        if instance.is_active:
            BaseAdvertisement.objects.exclude(pk=instance.pk).update(is_active=False)
