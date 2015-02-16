"""Contains tests for model Repository"""

# Python imports
from shutil import rmtree
from tempfile import mkdtemp
from unittest import skip

# app imports
from meissen.models import Repository
from meissen.tests import MeissenModelTestCase


class MeissenRepositoryModelTestCase(MeissenModelTestCase):

    def setUp(self):
        self.filesystem_path = mkdtemp()

    def tearDown(self):
        rmtree(self.filesystem_path)

    def test_unique_repo(self):
        skip
