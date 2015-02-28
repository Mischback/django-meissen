"""Contains views for a single repo"""

# Django imports
from django.shortcuts import get_object_or_404, render

# app imports
from meissen.util.repository_views import get_and_check_repo


def overview(request, repo_id):
    """The repository's landing page"""

    # Fetch the Repository
    repo = get_and_check_repo(request, repo_id)

    return render(request, 'meissen/repository/overview.html')
