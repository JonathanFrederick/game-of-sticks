"""A program to test the functions of sticks.py"""
import unittest
from sticks import *

class TestSticks(unittest.TestCase):
    def test_reset_dict(self):
        self.assertEqual(reset_dict({1:[1,2], 2:[2,3], 3:[1,3]}),
                                {1:[1,2,3], 2:[2,3,1], 3:[1,3,2]})
        self.assertEqual(reset_dict({1:[], 2:[], 3:[]}),
                                {1:[1,2,3], 2:[1,2,3], 3:[1,2,3]})
        self.assertEqual(reset_dict({1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}),
                                {1:[1,2,3], 2:[1,2,3], 3:[1,2,3]})

    def test_add_dict(self):
        self.assertEqual(add_dict([(1, 3),(2, 2),(3, 1)], {1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}),
                                {1:[1,2,3,3], 2:[1,2,3,2], 3:[1,2,3,1]})

    def test_subtract_dict(self):
        self.assertEqual(subtract_dict([(1, 3),(2, 2),(3, 1)], {1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}),
                                {1:[1,2], 2:[1,3], 3:[2,3]})

    def test_set_dict_range(self):
        self.assertEqual(set_dict_range(3, {}), {1:[1,2,3],2:[1,2,3],3:[1,2,3]})
        self.assertEqual(set_dict_range(3, {1:[1,2,3]}), {1:[1,2,3],2:[1,2,3],3:[1,2,3]})


if __name__ == '__main__':
    unittest.main()
