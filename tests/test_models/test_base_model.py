"""Test BaseModel"""

import unittest
from models.base_model import BaseModel
from time import sleep
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """command before each test unit"""
        pass

    def TearDown(self):
        """commands after each test unit"""
        pass

    def test_kwargs(self):
        """test the attributes dictionary"""
        ISO_format = "%Y-%m-%dT%H:%M:%S.%f"
        dic = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
               'created_at': '2017-09-28T21:03:54.052298',
               'my_number': 89,
               'updated_at': '2017-09-28T21:03:54.052302',
               'name': 'My_First_Model'}
        obj = BaseModel(**dic)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "my_number"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertEqual(obj.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(obj.created_at,
                         datetime.strptime(dic["created_at"], ISO_format))
        self.assertEqual(obj.updated_at,
                         datetime.strptime(dic["updated_at"], ISO_format))
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.name, 'My_First_Model')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_attributes(self):
        """Tests for attriutes"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, "id"))
        self.assertTrue(hasattr(obj1, "created_at"))
        self.assertTrue(hasattr(obj1, "updated_at"))
        self.assertIsInstance(obj1.created_at, datetime)
        self.assertIsInstance(obj1.updated_at, datetime)
        sleep(0.5)
        obj2 = BaseModel()
        obj2.name = "My First Model"
        obj2.number = 89
        self.assertTrue(hasattr(obj2, "id"))
        self.assertTrue(hasattr(obj2, "created_at"))
        self.assertTrue(hasattr(obj2, "updated_at"))
        self.assertTrue(hasattr(obj2, "name"))
        self.assertEqual(obj2.name, "My First Model")
        self.assertTrue(hasattr(obj2, "number"))
        self.assertEqual(obj2.number, 89)
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_str(self):
        """test the string format"""
        obj3 = BaseModel()
        self.assertTrue(hasattr(obj3, "id"))
        self.assertEqual(str(obj3),
                         f"[BaseModel] ({obj3.id}) {obj3.__dict__}")

    def test_save(self):
        """test the save method"""
        obj = BaseModel()
        obj.save()
        updated = obj.updated_at
        sleep(0.5)
        obj.save()
        self.assertNotEqual(obj.updated_at, updated)

    def test_to_dict(self):
        """test the dict format"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         obj.updated_at.isoformat())
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)


if __name__ == "__main__":
    unittest.main()
