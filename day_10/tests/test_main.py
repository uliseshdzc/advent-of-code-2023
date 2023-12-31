import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part_example_1(self):
        with patch("sys.argv", ["", "data\\example_1.txt", "1"]):
            self.assertEqual(main.main(), 4, "Should be 4")    

    def test_first_part_example_2(self):
        with patch("sys.argv", ["", "data\\example_2.txt", "1"]):
            self.assertEqual(main.main(), 8, "Should be 8")    

    def test_second_part_example_3(self):
        with patch("sys.argv", ["", "data\\example_3.txt", "2"]):
            self.assertEqual(main.main(), 4, "Should be 4")

    def test_second_part_example_4(self):
        with patch("sys.argv", ["", "data\\example_4.txt", "2"]):
            self.assertEqual(main.main(), 4, "Should be 4")

    def test_second_part_example_5(self):
        with patch("sys.argv", ["", "data\\example_5.txt", "2"]):
            self.assertEqual(main.main(), 8, "Should be 8")            

    def test_second_part_example_5(self):
        with patch("sys.argv", ["", "data\\example_6.txt", "2"]):
            self.assertEqual(main.main(), 10, "Should be 10")                    