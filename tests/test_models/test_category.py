#!/usr/bin/env python3
'''Test category for expected behavior and documentation'''
import inspect
import models
from models import category
from models.base_model import BaseModel
import pep8
import unittest
Category = category.Category


class TestCategoryDocs(unittest.TestCase):
    '''Tests to check the documentation and style of Category class'''
    @classmethod
    def setUpClass(cls):
        '''Set up for the doc tests'''
        cls.category_f = inspect.getmembers(Category, inspect.isfunction)

    def test_pep8_conformance_category(self):
        '''Test that models/category.py conforms to PEP8.'''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/category.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_category(self):
        '''Test that tests/test_models/test_category.py conforms to PEP8.'''
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_category.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_category_module_docstring(self):
        '''Test for the existence of module docstring'''
        self.assertIsNot(category.__doc__, None,
                         "category.py needs a docstring")
        self.assertTrue(len(category.__doc__) >= 1,
                        "category.py needs a docstring")

    def test_category_class_docstring(self):
        '''Test for the Category class docstring'''
        self.assertIsNot(Category.__doc__, None,
                         "Category class needs a docstring")
        self.assertTrue(len(Category.__doc__) >= 1,
                        "Category class needs a docstring")

    def test_category_func_docstrings(self):
        '''Test for the presence of docstrings in Category methods'''
        for func in self.category_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCategory(unittest.TestCase):
    '''Class for unittests of the category module'''
    def setUp(self):
        '''Set up for the tests'''
        self.c = Category(name="Test Category")

    def tearDown(self):
        '''Tear down for tests'''
        del self.c

    def test_is_subclass(self):
        '''Test that Category is a subclass of BaseModel'''
        self.assertTrue(issubclass(self.c.__class__, BaseModel), True)

    def test_has_attributes(self):
        '''Test that Category has attributes name'''
        self.assertTrue('name' in self.c.__dict__)

    def test_has_name_attr(self):
        '''Test that Category has attribute name, and it's an empty str'''
        self.assertTrue('name' in self.c.__dict__)
        self.assertEqual(type(self.c.name), str)

    def test_save_delete(self):
        '''Test that save and delete work'''
        self.c.save()
        self.assertTrue(hasattr(self.c, 'id'))
        self.c.delete()
        dict_keys = ['id', 'name', '__class__']
        self.assertEqual(sorted(self.c.to_dict().keys()), sorted(dict_keys))
        self.c.delete()
