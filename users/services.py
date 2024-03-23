from users.models import User
import uuid


def generate_code(prefix: str='') -> str:
    """Згенерувати випадковий UUID код (активація акаунта, зміна паролю)"""
    return str(f'{prefix}{uuid.uuid4().hex}')


def send_confirmation_email(user):
    """Відправити на почту `user` данні про активацію.
    :param user: об'єкт моделі User.
    """
    ...