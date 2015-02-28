"""Contains views for a single repo"""

# Django imports
from django.shortcuts import get_object_or_404, render

# app imports
from meissen.models import Repository


def overview(request, repo_id):
    """The repository's landing page"""

    # Fetch the Repository
    # TODO: Do we really want to use this shortcut?
    repo = get_object_or_404(Repository, pk=repo_id)

    # Has the current user read access?
    if request.user.meissen_user_set.read_users_set.filter(pk=repo_id):
        print request.user

    return render(request, 'meissen/repository/overview.html')
