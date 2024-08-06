"""
Testing Framework: Unittest

Tested:
- '__version__': Unit tests for the project's version.
- 'src.models.user.User': Unit tests for the 'User' model class.
"""

import os
import unittest
from datetime import datetime
from src import __version__
from src.models.user import User
from src.managers.db import DB


class TestSrcVersion(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    
    def test_version(self):
        """
        Test the project version (__version__) against an expected value.
        """
        self.assertEqual(__version__, "0.1")


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up a 'User' instance with sample attribute values for testing.
        """
        self.user = User()
        self.user.username = "tester"
        self.user.password = "tester"
        self.user.email = "tester"
        self.user.is_admin = False
        return super().setUp()

    
    def test_user_object_instantiation(self):
        """
        Test the instantiation of a 'User' object and check its attributes.
        """
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, "tester")
        self.assertEqual(self.user.password, "tester")
        self.assertEqual(self.user.email, "tester")
        self.assertFalse(self.user.is_admin)


    def test_user_object_datetime_attribute(self):
        """
        Test the 'created' attribute of a 'User' object for existence and data type.
        """
        self.assertIsNotNone(self.user.created)
        self.assertIsInstance(self.user.created, datetime)


    def test_user_object_attributes_setter(self):
        """
        Test the setter methods for 'User' attributes and verify their values.
        """
        self.user.username = "tester2"
        self.user.password = "tester2"
        self.user.email = "tester2"
        self.user.is_admin = True

        self.assertEqual(self.user.username, "tester2")
        self.assertEqual(self.user.password, "tester2")
        self.assertEqual(self.user.email, "tester2")
        self.assertEqual(self.user.is_admin, True)

    
    def test_user_object_setter_raise_value_errors(self):
        """
        Test if setting 'User' attributes with incorrect types raises 'ValueError'.
        """
        with self.assertRaises(TypeError):
            self.user.username = 0
        with self.assertRaises(TypeError):
            self.user.password = 0
        with self.assertRaises(TypeError):
            self.user.email = 0
        with self.assertRaises(TypeError):
            self.user.is_admin = 0
        with self.assertRaises(TypeError):
            self.user.created = 0


    def test_user_object_attribute_validators(self):
        """
        Test the attribute validation functions for the 'User' model, specifically:
        - Username length validation
        - Valid character validation for username
        - Password length validation
        - No uppercase in password
        - No lowercase in password
        - No number in password
        - No symbol in password
        - Email address format validation

        Unique constraint validation to be added with DB integration.
        """
        with self.assertRaises(ValueError):
            User._validate_username("x"*51)             # Length validation
        with self.assertRaises(ValueError):
            User._validate_username(" ")                # Valid character validation
        with self.assertRaises(ValueError):
            User._validate_password("1")                # Length validation
        with self.assertRaises(ValueError):
            User._validate_password("abcdefghijk123!")  # No uppercase
        with self.assertRaises(ValueError):
            User._validate_password("ABCDEFGHIJK123!")  # No lowercase
        with self.assertRaises(ValueError):
            User._validate_password("Abcdefghijk!")     # No number
        with self.assertRaises(ValueError):
            User._validate_password("Abcdefghijk123")   # No symbol
        with self.assertRaises(ValueError):
            User._validate_email("inc@orr@ect@address") # Email Regex match


class TestDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_db_name = "test_database.db"
        cls.db = DB(db_name=cls.test_db_name)
        cls.db.create_user_table()
        
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()
        if os.path.exists(cls.test_db_name):
            os.remove(cls.test_db_name)

    
    def test_create_user_table(self):
        self.assertTrue(self.db.table_exists('User'))

    
    def test_create_user(self):
        self.db.create_user(
            "testuser",
            "password123",
            "test@example.com",
            False,
            '2024-01-01'
        )

        user = self.db.read_user(username="testuser")
        
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'testuser')
        self.assertEqual(user[2], 'password123')
        self.assertEqual(user[3], 'test@example.com')
        self.assertFalse(user[4])
        self.assertEqual(user[5], '2024-01-01')


    def test_read_user(self):
        self.db.create_user(
            "readtest",
            "pass",
            "readtest@example.com",
            False,
            "2023-01-01"
        )

        user = self.db.read_user(username="readtest")

        self.assertIsNotNone(user)
        self.assertEqual(user[1], "readtest")


    def test_update_user(self):
        self.db.create_user(
            'updatetest',
            'oldpass',
            'update@example.com',
            False, 
            '2023-01-01'
        )

        user = self.db.read_user(username='updatetest')
        user_id = user[0]

        self.db.update_user(user_id=user_id, username='newusername', password='newpass', email='newemail@example.com', is_admin=True)
        updated_user = self.db.read_user(username='newusername')
        
        self.assertEqual(updated_user[1], 'newusername')
        self.assertEqual(updated_user[2], 'newpass')
        self.assertEqual(updated_user[3], 'newemail@example.com')
        self.assertTrue(updated_user[4])



