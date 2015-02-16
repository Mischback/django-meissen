"""Hooks this app into Django's admin interface"""

# Django imports
from django.contrib import admin

# app imports
from meissen.models import RepositoryLocation

admin.site.register(RepositoryLocation)
