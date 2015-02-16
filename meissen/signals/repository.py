"""Contains signal handlers for the models of models/repository.py"""

# Python imports
from os import access, F_OK, R_OK, W_OK, X_OK, listdir
from os.path import join

# GitPython imports
from git.repo.fun import is_git_dir

# app imports
from meissen.exceptions import *
from meissen.models import Repository


def callback_check_repo_location(sender, instance, **kwargs):
    """Checks filesystem access to a given location"""

    # exists
    if not access(instance.path, F_OK):
        raise MeissenNotExistingPathException

    # readable
    if not access(instance.path, R_OK):
        raise MeissenNoReadAccessException

    # writeable
    if not access(instance.path, W_OK):
        raise MeissenNoWriteAccessException

    # executable
    if not access(instance.path, X_OK):
        raise MeissenNoExecuteAccessException


def callback_find_existing_repos(sender, instance, **kwargs):
    """Finds existing repositories in a given location"""

    for item in listdir(instance.path):
        if is_git_dir(join(instance.path, item)):
            Repository.objects.create(
                path = instance,
                filesystem_name = item,
            )
