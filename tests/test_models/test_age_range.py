#!/usr/bin/env python3
"""Test BaseModel for expected behavior and documentation"""
import inspect
import models
from models import age_range
import pep8 as pycodestyle
import time
import unittest
from unittest.mock import patch
AgeRange = age_range.AgeRange


class TestAgeRangeDocs(unittest.TestCase):
    """Tests to check the documentation and style of AgeRange class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.age_range_funcs = inspect.getmembers(AgeRange, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/age_range.py conforms to PEP8."""
        for path in ['models/age_range.py',
                     'tests/test_models/test_age_range.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(age_range.__doc__, None,
                         "age_range.py needs a docstring")
        self.assertTrue(len(age_range.__doc__) > 1,
                        "age_range.py needs a docstring")

    def test_class_docstring(self):
        """Test for the AgeRange class docstring"""
        self.assertIsNot(AgeRange.__doc__, None,
                         "AgeRange class needs a docstring")
        self.assertTrue(len(AgeRange.__doc__) >= 1,
                        "AgeRange class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in AgeRange methods"""
        for func in self.age_range_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestAgeRange(unittest.TestCase):
    """Class for unittests of the age_range module"""
    def setUp(self):
        """Set up for the tests"""
        self.age_range = AgeRange()
        self.age_range.age_from = 1
        self.age_range.age_to = 2

    def test_isinstance(self):
        """Test that age_range is an instance of AgeRange"""
        self.assertIsInstance(self.age_range, AgeRange)

    def test_attributes(self):
        """Test that age_range has the required attributes"""
        self.assertTrue(hasattr(self.age_range, 'age_from'))
        self.assertTrue(hasattr(self.age_range, 'age_to'))

    def test_attributes_type(self):
        """Test that age_range has the required attribute types"""
        self.assertEqual(type(self.age_range.age_from), int)
        self.assertEqual(type(self.age_range.age_to), int)

    def test_str(self):
        """Test that the str method has the correct output"""
        self.assertEqual(str(self.age_range),
                         "[[{}] ({}) from {} to {}]".format(
                             self.age_range.__class__.__name__,
                             self.age_range.id,
                             self.age_range.age_from,
                             self.age_range.age_to))

    def test_save_delelte(self):
        """Test that the save and delete methods work"""
        self.age_range.save()
        self.assertTrue(hasattr(self.age_range, 'id'))
        self.age_range.delete()

    def test_to_dict(self):
        """Test that the to_dict method has the correct output"""
        self.assertEqual(self.age_range.to_dict(),
                         {'id': self.age_range.id,
                          'age_from': self.age_range.age_from,
                          'age_to': self.age_range.age_to,
                          '__class__': self.age_range.__class__.__name__})
