"""Contains views for a single repo"""

# Django imports
from django.shortcuts import get_object_or_404, render

# app imports
from meissen.models import Repository


def overview(req, repo_id):
    """The repository's landing page"""

    repo = get_object_or_404(Repository, pk=repo_id)

    return render(req, 'meissen/repository/overview.html')
