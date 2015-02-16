"""Contains views for a single repo"""

# Django imports
from django.shortcuts import render


def overview(req, repo_id):
    """The app's landing page"""
    return render(req, 'meissen/home.html')
