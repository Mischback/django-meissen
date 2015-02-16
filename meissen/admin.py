"""Hooks this app into Django's admin interface"""

# Django imports
from django.contrib import admin

# app imports
from meissen.models import RepositoryLocation, Repository
from meissen.models.repository_location import RepositoryLocationAdmin

admin.site.register(RepositoryLocation, RepositoryLocationAdmin)
admin.site.register(Repository)
