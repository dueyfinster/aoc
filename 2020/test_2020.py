import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import Day1, Day2, Day3

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

class Day2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 2)
        file = advent.read_file()
        self.data = Day2.process_input(helper.get_lines(file))

    def test_day_one_part_one(self):
        self.assertEqual(Day2.part1(self.data), 500)
    
    def test_day_two_part_one(self):
        self.assertEqual(Day2.part2(self.data), 313)

class Day3Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 3)
        file = advent.read_file()
        self.data = helper.get_lines(file)

    def test_day_one_part_one(self):
        self.assertEqual(Day3.part1(self.data), 218)
    
    def test_day_two_part_one(self):
        self.assertEqual(Day3.part2(self.data), 3847183340)

if __name__ == '__main__':
    unittest.main()
