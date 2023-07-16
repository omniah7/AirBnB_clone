"""Test BaseModel"""

import unittest
from models.base_model import BaseModel

class test_BaseModel(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """create two test instances"""
        pass

    def TearDown(self):
        """ delete json file """
        pass

    def test_attributes(self):
        """Tests for attriutes"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, "id"))
        self.assertTrue(hasattr(obj1, "created_at"))
        self.assertTrue(hasattr(obj1, "updated_at"))
        obj2 = BaseModel()
        self.assertTrue(hasattr(obj2, "id"))
        self.assertTrue(hasattr(obj2, "created_at"))
        self.assertTrue(hasattr(obj2, "updated_at"))
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        

    def test_str(self):
        """test the string format"""
        obj3 = BaseModel()
        self.assertTrue(hasattr(obj3, "id"))
        self.assertEqual(str(obj3), f"[BaseModel] ({obj3.id}) {obj3.__dict__}")

    def test_to_dict(self):
        """test the dict format"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['created_at']), str)

