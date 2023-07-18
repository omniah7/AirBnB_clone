"""Test Amenity"""

import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """Test Amenity Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_attributes(self):
        """tests the attribute"""
        o = Amenity()
        self.assertTrue(hasattr(o, 'name'))
        self.assertIsInstance(o.name, str)
        o.name = "AlX"
        self.assertEqual(o.name, 'AlX')


if __name__ == "__main__":
    unittest.main()
