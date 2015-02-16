"""Contains basic views"""

# Django imports
from django.shortcuts import render


def home(req):
    """The app's landing page"""
    return render(req, 'meissen/home.html')
