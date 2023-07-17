"""Test FileStorage"""

import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_FileStorage(unittest.TestCase):
    """Test BaseModel Class"""
    def setUp(self):
        """commands before each test unit"""
        """try:
            print(f"{os.find('file_storage.py')}/{storage.__file_path}")
            os.remove(f"{os.pwd(storage)}/{storage.__file_path}")
        except:
            pass"""

    def TearDown(self):
        """commands after each test unit"""
        # os.remove(f"{os.pwd(storage)}/{storage.__file_path}")

    def test_cls_attributes(self):
        """test the class attributes"""
        obj1 = BaseModel()
        objects = storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIs(objects[f"BaseModel.{obj1.id}"], obj1)
        obj2 = BaseModel()
        objects = storage.all()
        self.assertIs(objects[f"BaseModel.{obj2.id}"], obj2)
        self.assertEqual(len(objects), 2)

    def test_self_attributes(self):
        """test the instance attributes"""
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()


if __name__ == "__main__":
    unittest.main()
