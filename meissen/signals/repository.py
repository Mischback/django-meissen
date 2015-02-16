"""Contains signal handlers for the models of models/repository.py"""

# Python imports
from os import access, F_OK, R_OK, W_OK, X_OK

# app imports
from meissen.exceptions import *


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
