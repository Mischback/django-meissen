"""These classes represent repositories irl"""

# Django imports
from django.db import models


class Repository(models.Model):
    """Represents a single Repository"""

    name = models.CharField(max_length=255, default='foo')
    """Name of the repository"""

    path = models.ForeignKey('RepositoryLocation')
    """Foreign key to a RepositoryLocation object"""

    filesystem_name = models.CharField(max_length=100)
    """Name on the filesystem"""

    def __unicode__(self):
        return '[{0}] {1} - {2}{3}'.format(
            self._meta.verbose_name,
            self.name,
            self.path.path,
            self.filesystem_name)

    class Meta:
        app_label = 'meissen'
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
        unique_together = ('path', 'filesystem_name')
