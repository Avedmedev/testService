from django.apps import AppConfig


class myTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myTest'
    verbose_name = 'Тестирование'
