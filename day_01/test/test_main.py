import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part(self):
        with patch("sys.argv", ["", "data\\example_1.txt", "1"]):
            self.assertEqual(main.main(), 142, "Should be 142")

    def test_second_part(self):
        with patch("sys.argv", ["", "data\\example_2.txt", "2"]):
            self.assertEqual(main.main(), 281, "Should be 281")