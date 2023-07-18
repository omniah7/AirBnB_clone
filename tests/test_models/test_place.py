"""Test Place"""

import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """Test Place Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_attributes(self):
        """tests the attribute"""
        o = Place()
        self.assertTrue(hasattr(o, 'name'))
        self.assertTrue(hasattr(o, 'city_id'))
        self.assertTrue(hasattr(o, 'user_id'))
        self.assertTrue(hasattr(o, 'description'))
        self.assertTrue(hasattr(o, 'number_rooms'))
        self.assertTrue(hasattr(o, 'number_bathrooms'))
        self.assertTrue(hasattr(o, 'max_guest'))
        self.assertTrue(hasattr(o, 'price_by_night'))
        self.assertTrue(hasattr(o, 'latitude'))
        self.assertTrue(hasattr(o, 'longitude'))
        self.assertTrue(hasattr(o, 'amenity_ids'))
        self.assertIsInstance(o.name, str)
        self.assertIsInstance(o.city_id, str)
        self.assertIsInstance(o.user_id, str)
        self.assertIsInstance(o.description, str)
        self.assertIsInstance(o.number_rooms, int)
        self.assertIsInstance(o.number_bathrooms, int)
        self.assertIsInstance(o.max_guest, int)
        self.assertIsInstance(o.price_by_night, int)
        self.assertIsInstance(o.latitude, float)
        self.assertIsInstance(o.longitude, float)
        self.assertIsInstance(o.amenity_ids, list)
        o.name = "AlX"
        self.assertEqual(o.name, 'AlX')


if __name__ == "__main__":
    unittest.main()
