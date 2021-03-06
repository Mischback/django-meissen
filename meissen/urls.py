"""Django url configuration

This file contains app specific urls, so that they are decoupled from the 
projects main url configuration.
"""

# Django imports
from django.conf.urls import patterns, url

# Basic views (views/basic.py)
urlpatterns = patterns('meissen.views.basic',
    url(r'^$', 'home', name='home'),
    url(r'^overview$', 'overview', name='basic.overview'),
)

# Repository views (views/repository.py)
urlpatterns += patterns('meissen.views.repository',
    url(r'^(?P<repo_id>\d+)/overview$', 'overview', name='repository.overview'),
)
