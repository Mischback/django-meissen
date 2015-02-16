"""Contains basic views"""

# Django imports
from django.shortcuts import render

# app imports
from meissen.models import Repository


def home(req):
    """The app's landing page"""
    return render(req, 'meissen/home.html')

def overview(req):
    """The app's landing page"""

    # get all repositories
    # TODO: Here is the place to limit access
    repos = Repository.objects.all()

    return render(req, 'meissen/overview.html',
        { 'repos': repos, },
    )
