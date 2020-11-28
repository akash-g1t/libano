from django.apps import AppConfig

class BankingConfig(AppConfig):
    name = 'banking'

    def ready(self):
        import banking.signals