from django.apps import AppConfig


class BuilderConfig(AppConfig):
    name = 'builder'

    def ready(self):
        import builder.signals
