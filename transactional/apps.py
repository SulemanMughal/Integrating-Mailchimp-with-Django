from django.apps import AppConfig


class TransactionalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transactional'
