import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import advent, helper
import Day1, Day2, Day3, Day4, Day5

class Day1Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 1)
        file = advent.read_file()
        self.nums = helper.get_ints(file)

    def test_day_one_part_one(self):
        self.assertEqual(Day1.part1(self.nums), 960075)
    
    def test_day_one_part_one(self):
        self.assertEqual(Day1.part2(self.nums), 212900130)

class Day2Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 2)
        file = advent.read_file()
        self.data = Day2.process_input(helper.get_lines(file))

    def test_day_two_part_one(self):
        self.assertEqual(Day2.part1(self.data), 500)
    
    def test_day_two_part_one(self):
        self.assertEqual(Day2.part2(self.data), 313)

class Day3Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 3)
        file = advent.read_file()
        self.data = helper.get_lines(file)

    def test_day_three_part_one(self):
        self.assertEqual(Day3.part1(self.data), 218)
    
    def test_day_three_part_one(self):
        self.assertEqual(Day3.part2(self.data), 3847183340)


class Day4Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 4)
        file = advent.read_file()
        self.data = Day4.process_input(helper.get_lines(file))

    @unittest.skip("Fix return value")
    def test_day_four_part_one(self):
        self.assertEqual(Day4.part1(self.data), 228)
    
    def test_day_four_part_two(self):
        self.data = Day4.part1(self.data) # Needs data from part1
        self.assertEqual(Day4.part2(self.data), 175)

class Day5Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        advent.setup(2020, 5)
        file = advent.read_file()
        self.data = Day5.process_input(helper.get_lines(file))

    @unittest.skip("Fix return value")
    def test_day_five_part_one(self):
        self.assertEqual(Day5.part1(self.data), 980)
    
    def test_day_five_part_two(self):
        self.data = Day5.part1(self.data) # Needs data from part1
        self.assertEqual(Day5.part2(self.data), 607)

if __name__ == '__main__':
    unittest.main()
