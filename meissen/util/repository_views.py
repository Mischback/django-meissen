"""Contains some utility functions for repository views"""

# Django imports
from django.shortcuts import get_object_or_404

# app imports
from meissen.exceptions import MeissenAccessDeniedException
from meissen.models import Repository

def get_and_check_repo(request, repo_id):

    # Fetch the Repository
    # TODO: Do we want to use this shortcut? Or are we going to work with our custom exceptions?
    repo = get_object_or_404(Repository, pk=repo_id)

    try:
        # Has the current user read access?
        # TODO: Make this PEP8!!!
        if not (repo.public_repo or request.user.meissen_user_set.read_users_set.filter(pk=repo_id)):
            raise MeissenAccessDeniedException('No read access')
    except AttributeError:
        raise MeissenAccessDeniedException('Caught AttributeError')

    return None
