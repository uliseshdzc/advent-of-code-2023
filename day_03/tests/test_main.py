import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "1"]):
            self.assertEqual(main.main(), 4361, "Should be 4361")

    def test_second_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "2"]):
            self.assertEqual(main.main(), 467835, "Should be 467835")