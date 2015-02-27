"""Hooks this app into Django's admin interface"""

# Django imports
from django.contrib import admin

# app imports
from meissen.models import MeissenUser, Repository, RepositoryLocation
from meissen.models.repository_location import RepositoryLocationAdmin

admin.site.register(MeissenUser)
admin.site.register(Repository)
admin.site.register(RepositoryLocation, RepositoryLocationAdmin)
