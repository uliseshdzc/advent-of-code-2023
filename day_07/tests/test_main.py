import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "1"]):
            self.assertEqual(main.main(), 6440, "Should be 6440")

    def test_second_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "2"]):
            self.assertEqual(main.main(), 5905, "Should be 5905")