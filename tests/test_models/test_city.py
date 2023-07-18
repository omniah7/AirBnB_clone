"""Test City"""

import unittest
from models.city import City


class test_City(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_attributes(self):
        """tests the attribute"""
        c = City()
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)
        c.state_id = "123-id"
        c.name = "AlX"
        self.assertEqual(c.state_id, '123-id')
        self.assertEqual(c.name, 'AlX')


if __name__ == "__main__":
    unittest.main()
