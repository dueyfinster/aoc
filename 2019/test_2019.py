import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from . import Day1, Day2

class Day1Tests(unittest.TestCase):
    def test_day_one_part_one(self):
        self.assertEqual(Day1.part_one(), 3432671)
    
    def test_day_one_part_two(self):
        self.assertEqual(Day1.part_two(), 5146132)

class Day2Tests(unittest.TestCase):
    def test_day_two_part_one(self):
        self.assertEqual(Day2.part_one(), 3306701)
    
    def test_day_two_part_two(self):
        self.assertEqual(Day2.part_two(), 7621)

if __name__ == '__main__':
    unittest.main()
