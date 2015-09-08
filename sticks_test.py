"""A program to test the functions of sticks.py"""
import unittest
from sticks import *

class TestSticks(unittest.TestCase):
    pass

def test_reset_dict(self):
    self.assertEqual(reset_dict({"HI":{1:[1,2], 2:[2,3], 3:[1,3]}},
                            {"HI":{1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}}))
    self.assertEqual(reset_dict({"HI":{1:[], 2:[], 3:[]}}, ))
                            {"HI":{1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}}))
    self.assertEqual(reset_dict({"HI":{1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}}, 
                            {"HI":{1:[1,2,3], 2:[1,2,3], 3:[1,2,3]}}))

if __name__ == '__main__':
    unittest.main()
