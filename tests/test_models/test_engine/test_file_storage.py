"""Test FileStorage"""

import unittest
from models import storage


class test_FileStorage(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """commands before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_cls_attributes(self):
        """test the class attributes"""
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))

    def test_methods(self):
        """tests for reload"""
        pass


if __name__ == "__main__":
    unittest.main()
