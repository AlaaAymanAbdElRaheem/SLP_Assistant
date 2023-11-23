#!/usr/bin/env python3
'''
Module that contains unittests for the DB storage
'''
import unittest
import inspect
import pep8
import models
from models.base_model import BaseModel
from models.child_milestones import ChildMilestones
from models.engine import db_storage


DBStorage = db_storage
classes = {"ChildMilestones": ChildMilestones, "BaseModel": BaseModel}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

# class TestDBStorage(unittest.TestCase):
#     '''Test if DB Storage is working correctly'''
#     def setUp(self):
#         '''Set up method'''
#         self.db = DBStorage
#         self.db.reload()

#     def tearDown(self):
#         '''Tear down method'''
#         self.db.close()

#     def test_create(self):
#         '''Test if we can create an object'''
#         new_base = BaseModel()
#         new_base.name = "SLP"
#         new_base.save()
#         self.assertTrue(new_base.id in models.storage.all())

#     def test_delete(self):
#         '''Test if we can delete an object'''
#         new_base = BaseModel()
#         new_base.name = "SLP"
#         new_base.save()
#         self.assertTrue(new_base.id in models.storage.all())
#         self.db.delete(new_base)
#         self.assertFalse(new_base.id in models.storage.all())
