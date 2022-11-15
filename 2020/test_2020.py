import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import Day1

class Day1Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 1)
        file = advent.read_file()
        self.nums = helper.get_ints(file)

    def test_day_one_part_one(self):
        self.assertEqual(Day1.part1(self.nums), 960075)
    
    def test_day_two_part_one(self):
        self.assertEqual(Day1.part2(self.nums), 212900130)



if __name__ == '__main__':
    unittest.main()
