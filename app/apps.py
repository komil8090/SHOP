from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals

