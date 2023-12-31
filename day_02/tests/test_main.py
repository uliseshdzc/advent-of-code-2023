import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_first_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "1"]):
            self.assertEqual(main.main(), 8, "Should be 8")

    def test_second_part(self):
        with patch("sys.argv", ["", "data\\example.txt", "2"]):
            self.assertEqual(main.main(), 2286, "Should be 2286")