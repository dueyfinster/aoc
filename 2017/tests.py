import unittest
import Day1

class Tests(unittest.TestCase):

    def test_day_one_part_one(self):
        self.assertEqual(Day1.part_one(), 1223)
        
    def test_day_two_part_one(self):
        self.assertEqual(Day1.part_two(), 1284)


if __name__ == '__main__':
    unittest.main()
