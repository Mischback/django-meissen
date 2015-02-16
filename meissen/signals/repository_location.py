"""Contains signal handlers for the models of models/repository.py"""

# Python imports
from os import listdir
from os.path import join

# GitPython imports
from git.repo.fun import is_git_dir

# app imports
from meissen.models import Repository


def callback_find_existing_repos(sender, instance, **kwargs):
    """Finds existing repositories in a given location"""

    for item in listdir(instance.path):
        if is_git_dir(join(instance.path, item)):
            Repository.objects.create(
                path = instance,
                filesystem_name = item,
            )
