"""Test User"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class test_User(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_attributes(self):
        """tests the attribute"""
        my_user = User()
        self.assertTrue(hasattr(my_user, 'first_name'))
        self.assertTrue(hasattr(my_user, 'last_name'))
        self.assertTrue(hasattr(my_user, 'email'))
        self.assertTrue(hasattr(my_user, 'password'))
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        self.assertEqual(my_user.first_name, 'Betty')
        self.assertEqual(my_user.last_name, 'Bar')
        self.assertEqual(my_user.email, 'airbnb@mail.com')
        self.assertEqual(my_user.password, 'root')


if __name__ == "__main__":
    unittest.main()
