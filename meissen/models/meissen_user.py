"""Contains an app specific extension of the Django User model"""

# Django imports
from django.conf import settings
from django.db import models

class MeissenUser(models.Model):
    """Connects Django users to Repository objects"""

    django_user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='meissen_user_set')
    """A OneToOneField to the used AUTH_USER_MODEL"""

    def __unicode__(self):
        return '[MeissenUser] {0}'.format(self.django_user.username)

    class Meta:
        app_label = 'meissen'
        verbose_name = 'MeissenUser'
        verbose_name_plural = 'MeissenUsers'
