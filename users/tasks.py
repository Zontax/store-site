from django.contrib.auth import get_user_model
from celery import shared_task

from datetime import timedelta
from users.models import User

@shared_task
def clear_activation_key(user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.activation_key = None
        user.save()
        print(f'Секретний ключ {user.username} очищено')
    except User.DoesNotExist:
        print('User does not exist')
