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
        self.user.username = "tester"
        self.user.password = "tester"
        self.user.email = "tester"
        self.user.is_admin = False

        return super().setUp()

    
    def test_user_object_instantiation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, "tester")
        self.assertEqual(self.user.password, "tester")
        self.assertEqual(self.user.email, "tester")
        self.assertFalse(self.user.is_admin)


    def test_user_object_datetime_attribute(self):
        self.assertIsNotNone(self.user.created)
        self.assertIsInstance(self.user.created, datetime)


    def test_user_object_attributes_setter(self):
        self.user.__setattr__("username", "tester")
        self.user.__setattr__("password", "tester")
        self.user.__setattr__("email", "tester")
        self.user.__setattr__("is_admin", True)

        self.assertEqual(self.user.username, "tester")
        self.assertEqual(self.user.password, "tester")
        self.assertEqual(self.user.email, "tester")
        self.assertEqual(self.user.is_admin, True)

    
    def test_user_object_setter_raise_value_errors(self):
        with self.assertRaises(ValueError):
            self.user.__setattr__("username", 0)
            self.user.__setattr__("password", 0)
            self.user.__setattr__("email", 0)
            self.user.__setattr__("is_admin", 0)
            self.user.__setattr__("created", 0)
        
