import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from . import Day1, Day2

class Day1Tests(unittest.TestCase):

    def test_day_one_part_one(self):
        self.assertEqual(Day1.part_one(), 1223)
        
    def test_day_two_part_one(self):
        self.assertEqual(Day1.part_two(), 1284)

class Day2Tests(unittest.TestCase):
    @unittest.skip("Need to refactor impl")
    def test_part_one(self):
        self.assertEqual(Day2.part_one(), 34581)
    
    @unittest.skip("Need to refactor impl")
    def test_part_two(self):
        self.assertEqual(Day2.part_two(), 214)



if __name__ == '__main__':
    unittest.main()
