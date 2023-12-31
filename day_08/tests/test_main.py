import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part_example_1(self):
        with patch("sys.argv", ["", "data\\example_1.txt", "1"]):
            self.assertEqual(main.main(), 2, "Should be 2")    
            
    def test_first_part_example_2(self):
        with patch("sys.argv", ["", "data\\example_2.txt", "1"]):
            self.assertEqual(main.main(), 6, "Should be 6")

    def test_second_part(self):
        with patch("sys.argv", ["", "data\\example_3.txt", "2"]):
            self.assertEqual(main.main(), 6, "Should be 6")