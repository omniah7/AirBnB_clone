"""Test FileStorage"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import shutil


class test_FileStorage(unittest.TestCase):
    """Test BaseModel Class"""
    @classmethod
    def setUpClass(cls):
        """run setUp code just once before all tests"""
        cls.file = 'file.json'
        if (os.path.exists(cls.file)):
            shutil.copy(cls.file, 'default.json')
        with open(cls.file, 'w') as f:
            f.truncate()

    @classmethod
    def tearDownClass(cls):
        # run teardown code just once after all tests
        os.remove(cls.file)
        try:
            os.rename('default.json', cls.file)
        except FileNotFoundError:
            pass

    def setUp(self):
        """commands before each test unit"""
        self.storage = FileStorage()
        self.file = 'file.json'

    def tearDown(self):
        """commands after each test unit"""
        del self.storage

    def test_cls_attributes(self):
        """test the class attributes"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(isinstance(self.storage._FileStorage__file_path, str))

    def test_reload(self):
        """tests for reload"""
        with open(self.file, '+w') as f:
            text = '{"BaseModel.22222222-b69c-42f9-b818-0722de86ab37": ' \
                   + '{"id": "22222222-b69c-42f9-b818-0722de86ab37", ' \
                   + '"created_at": "2022-07-18T16:24:17.464453", ' \
                   + '"updated_at": "2022-07-18T16:24:17.468240", ' \
                   + '"__class__": "BaseModel"}}'
            f.write(text)
        self.storage.reload()
        objs = self.storage._FileStorage__objects
        self.assertIn("BaseModel.22222222-b69c-42f9-b818-0722de86ab37",
                      objs)

    def test_all(self):
        """tests for all"""
        all = self.storage.all()
        self.assertEqual(dict, type(all))

    def test_new(self):
        """tests for new"""
        o = BaseModel()
        objs = self.storage._FileStorage__objects
        self.assertIn("BaseModel." + o.id, objs)

    def test_save(self):
        """tests for save"""
        dic = {"id": "11111111-b69c-42f9-b818-0722de86ab37",
               "created_at": "2023-07-18T16:24:17.464453",
               "updated_at": "2023-07-18T16:24:17.468240",
               "__class__": "BaseModel"}
        o = BaseModel(**dic)
        self.storage.new(o)
        self.storage.save()
        with open(self.file, 'r') as f:
            r = f.read()
            self.assertIn("BaseModel.11111111-b69c-42f9-b818-0722de86ab37", r)


if __name__ == "__main__":
    unittest.main()
