#!/usr/bin/env python3
'''Test child_milestone for expected behavior and documentation'''
import inspect
import models
from models import child_milestone
from models import category
from models import age_range
from models.base_model import BaseModel
import pep8
import unittest
ChildMilestone = child_milestone.ChildMilestone


class TestChildMilestoneDocs(unittest.TestCase):
    '''Tests to check the documentation and style of ChildMilestone class'''
    @classmethod
    def setUpClass(cls):
        '''Set up for the doc tests'''
        cls.child_milestone_f = inspect.getmembers(
            ChildMilestone, inspect.isfunction)

    def test_pep8_conformance_child_milestone(self):
        '''Test that models/child_milestone.py conforms to PEP8.'''
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(['models/child_milestone.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_child_milestone(self):
        '''Test that test_child_milestone.py conforms to PEP8.'''
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(
            ['tests/test_models/test_child_milestones.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_child_milestone_module_docstring(self):
        '''Test for the existence of module docstring'''
        self.assertIsNot(child_milestone.__doc__, None,
                         "child_milestone.py needs a docstring")
        self.assertTrue(len(child_milestone.__doc__) >= 1,
                        "child_milestone.py needs a docstring")

    def test_child_milestone_class_docstring(self):
        '''Test for the ChildMilestone class docstring'''
        self.assertIsNot(ChildMilestone.__doc__, None,
                         "ChildMilestone class needs a docstring")
        self.assertTrue(len(ChildMilestone.__doc__) >= 1,
                        "ChildMilestone class needs a docstring")

    def test_child_milestone_func_docstrings(self):
        '''Test for the presence of docstrings in ChildMilestone methods'''
        for func in self.child_milestone_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestChildMilestone(unittest.TestCase):
    '''Class for unittests of the child_milestone module'''
    def setUp(self):
        '''Set up for the tests'''
        self.milestone = ChildMilestone(value="Test ChildMilestone")

    def tearDown(self):
        '''Tear down for tests'''
        del self.milestone

    def test_is_subclass(self):
        '''Test that ChildMilestone is a subclass of BaseModel'''
        self.assertTrue(issubclass(self.milestone.__class__, BaseModel), True)

    def test_attribute_types(self):
        '''Test that ChildMilestone has attr type'''
        self.assertEqual(type(self.milestone.value), str)

    def test_has_attributes(self):
        '''Test that ChildMilestone has attributes'''
        self.assertTrue('value' in self.milestone.__dict__)

    def test_save_delete(self):
        '''test save and delete'''
        category1 = category.Category(name="Test Category")
        age_range1 = age_range.AgeRange(age_from=1, age_to=2)
        category1.save()
        age_range1.save()
        self.milestone.category_id = category1.id
        self.milestone.age_range_id = age_range1.id
        self.milestone.save()
        self.assertTrue(hasattr(self.milestone, 'id'))
        dict_keys = ['id', 'type', 'age_from', 'age_to', 'value', '__class__']
        self.assertEqual(sorted(self.milestone.to_dict().keys()),
                         sorted(dict_keys))
        self.milestone.delete()
