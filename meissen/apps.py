# Django imports
from django.apps import AppConfig


class MeissenConfig(AppConfig):
    """App specific configuration class"""

    name = 'meissen'
    """Default name of this app"""

    verbose_name = 'Meissen'
    """The app's name in frontends"""
