"""These classes represent repositories irl"""

# Django imports
from django.db import models


class RepositoryLocation(models.Model):
    """Represents a filesystem location where repositories are stored"""

    path = models.CharField(max_length=255, unique=True, default='/tmp/')
    """The file system path (given from /)"""
    # TODO: enforce trailing slash!
    # TODO: Windows compatibility?!

    def __unicode__(self):
        return '[{0}] {1}'.format(self._meta.verbose_name, self.path)

    class Meta:
        app_label = 'meissen'
        verbose_name = 'RepositoryLocation'
        verbose_name_plural = 'RepositoryLocations'
