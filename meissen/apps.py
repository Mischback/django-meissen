"""Application configuration

This is a new feature of Django 1.7, so I don't know if using this will
make this app unusable in prior versions.
See: https://docs.djangoproject.com/en/1.7/ref/applications/ for details.
"""
# Django imports
from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save

# app imports
from meissen.models import RepositoryLocation
from meissen.signals.repository_location import callback_find_existing_repos


class MeissenConfig(AppConfig):
    """App specific configuration class"""

    name = 'meissen'
    """Default name of this app"""

    verbose_name = 'Meissen'
    """The app's name in frontends"""

    def ready(self):
        """Executed when application loading is completed"""

        post_save.connect(callback_find_existing_repos,
            sender=RepositoryLocation,
            weak=False,
            dispatch_uid='models.repository.find_existing_repos')
