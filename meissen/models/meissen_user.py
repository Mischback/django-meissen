"""Contains an app specific extension of the Django User model"""

# Django imports
from django.conf import settings
from django.db import models

class MeissenUser(models.Model):

    django_user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='meissen_user_set')

    def __unicode__(self):
        return '[MeissenUser] {0}'.format(self.django_user.username)

    class Meta:
        app_label = 'meissen'
        verbose_name = 'MeissenUser'
        verbose_name_plural = 'MeissenUsers'
