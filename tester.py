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
        self.user.username = "tester2"
        self.user.password = "tester2"
        self.user.email = "tester2"
        self.user.is_admin = True

        self.assertEqual(self.user.username, "tester2")
        self.assertEqual(self.user.password, "tester2")
        self.assertEqual(self.user.email, "tester2")
        self.assertEqual(self.user.is_admin, True)

    
    def test_user_object_setter_raise_value_errors(self):
        with self.assertRaises(TypeError):
            self.user.username = 0
            self.user.password = 0
            self.user.email = 0
            self.user.is_admin = 0
            self.user.created = 0


    def test_user_object_attribute_validators(self):
        # Unique constraint validation to be added with DB integration
        with self.assertRaises(ValueError):
            User._validate_username("x"*51)             # Length validation
            User._validate_username(" ")                # Valid character validation
            User._validate_password("1")                # Length validation
            User._validate_password("abcdefghijk123!")  # No uppercase
            User._validate_password("ABCDEFGHIJK123!")  # No lowercase
            User._validate_password("Abcdefghijk!")     # No number
            User._validate_password("Abcdefghijk123")   # No symbol
            User._validate_email("inc@orr@ect@address")