"""Contains tests for model RepositoryLocation"""

# Python imports
from os import chmod
from shutil import rmtree
from tempfile import mkdtemp
from unittest import skip

# Django imports
from django.db import IntegrityError

# app imports
from meissen.exceptions import *
from meissen.models import RepositoryLocation
from meissen.tests import MeissenModelTestCase


class MeissenRepositoryLocationModelTestCase(MeissenModelTestCase):

    def setUp(self):
        self.filesystem_path = mkdtemp()

    def tearDown(self):
        rmtree(self.filesystem_path)

    def test_unique_path(self):
        """Test the uniqueness of the path

        Meaning: There must not be two RepositoryLocation objects with
        identical path attributes. This is enforced by using Django's CharField
        unique attribute. Let's just see if this works.
        """
        with self.assertRaises(IntegrityError):
            a = RepositoryLocation.objects.create(path=self.filesystem_path)
            b = RepositoryLocation.objects.create(path=self.filesystem_path)

    def test_enforce_trailing_slash(self):
        """The path attribute must have a trailing slash."""
        # TODO: Must be implemented when the feature is implemented in model
        skip

    def test_signal_check_repo_location(self):
        """Test the correctness of the callback functions."""
        # test existence
        with self.assertRaises(MeissenNotExistingPathException):
            a = RepositoryLocation.objects.create(path='meissen{0}'.format(self.filesystem_path))

        # readable
        chmod(self.filesystem_path, 0000)
        with self.assertRaises(MeissenNoReadAccessException):
            a = RepositoryLocation.objects.create(path=self.filesystem_path)

        # writeable
        chmod(self.filesystem_path, 0400)
        with self.assertRaises(MeissenNoWriteAccessException):
            a = RepositoryLocation.objects.create(path=self.filesystem_path)

        # executable
        chmod(self.filesystem_path, 0600)
        with self.assertRaises(MeissenNoExecuteAccessException):
            a = RepositoryLocation.objects.create(path=self.filesystem_path)
