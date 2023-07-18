"""Test Review"""

import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """Test Review Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_attributes(self):
        """tests the attribute"""
        o = Review()
        self.assertTrue(hasattr(o, 'text'))
        self.assertTrue(hasattr(o, 'place_id'))
        self.assertTrue(hasattr(o, 'user_id'))
        self.assertIsInstance(o.text, str)
        self.assertIsInstance(o.place_id, str)
        self.assertIsInstance(o.user_id, str)
        o.text = "AlX"
        o.place_id = '123-place-id'
        o.user_id = '123-user-id'
        self.assertEqual(o.text, 'AlX')
        self.assertEqual(o.place_id, '123-place-id')
        self.assertEqual(o.user_id, '123-user-id')


if __name__ == "__main__":
    unittest.main()
