import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import Day1, Day2

class Day1Tests(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        advent.setup(2019, 1)
        file = advent.read_file()
        self.content = helper.get_lines(file)
        
    def test_day_one_part_one(self):
        self.assertEqual(Day1.part1(self.content), 3432671)
    
    def test_day_one_part_two(self):
        self.assertEqual(Day1.part2(self.content), 5146132)

class Day2Tests(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        advent.setup(2019, 2)
        file = advent.read_file()
        self.content = helper.get_ints(file, True)
        self.content2 = self.content.copy()
        
    def test_day_two_part_one(self):
        self.assertEqual(Day2.part1(self.content), 3306701)
    
    def test_day_two_part_two(self):
        self.assertEqual(Day2.part2(self.content2), 7621)

if __name__ == '__main__':
    unittest.main()
