import unittest
from datetime import datetime
from src import __version__
from src.models.user import User


class TestSrcVersion(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    
    def test_version(self):
        self.assertEqual(__version__, "0.1")


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User()
        return super().setUp()

    
    def test_user_object_instantiation(self):
        self.assertIsInstance(self.user, User)
        self.assertIsNone(self.user.username)
        self.assertIsNone(self.user.password)
        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.is_admin)


    def test_user_object_datetime_attribute(self):
        self.assertIsNotNone(self.user.created)
        self.assertIsInstance(self.user.created, datetime)
    
