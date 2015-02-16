"""These classes represent repositories irl"""

# Python imports
from os import access, F_OK, R_OK, W_OK, X_OK, listdir

# Django imports
from django.contrib.admin import ModelAdmin
from django.db import models
from django.forms import ModelForm

# app imports
from meissen.exceptions import *


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


class RepositoryLocationAdminForm(ModelForm):
    """The form used in the Django admin menu"""

    def clean_path(self):
        """Makes some validation to the path field"""
        path = self.cleaned_data['path']

        # enforce the trailing slash
        if not path[-1:] == '/':
            path += '/'

        # check that location
        # exists
        if not access(path, F_OK):
            raise MeissenNotExistingPathException

        # readable
        if not access(path, R_OK):
            raise MeissenNoReadAccessException

        # writeable
        if not access(path, W_OK):
            raise MeissenNoWriteAccessException

        # executable
        if not access(path, X_OK):
            raise MeissenNoExecuteAccessException

        # returned the validated path
        self.cleaned_data['path'] = path
        return self.cleaned_data['path']


class RepositoryLocationAdmin(ModelAdmin):

    form = RepositoryLocationAdminForm
