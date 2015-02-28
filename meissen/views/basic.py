"""Contains basic views"""

# Django imports
from django.shortcuts import render

# app imports
from meissen.models import Repository


def home(request):
    """The app's landing page"""
    return render(request, 'meissen/home.html')

def overview(request):
    """The app's landing page"""

    # get all repositories
    # TODO: Here is the place to limit access
    repos = Repository.objects.all()

    return render(request, 'meissen/overview.html',
        { 'repos': repos, },
    )
