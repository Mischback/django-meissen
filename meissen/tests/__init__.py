# Django imports
from django.test import TestCase


class MeissenTestCase(TestCase):
    """Base class for all app specific tests"""
    pass

class MeissenModelTestCase(MeissenTestCase):
    """Base class for model tests"""
    pass
