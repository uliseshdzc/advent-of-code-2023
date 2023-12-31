import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_steps_6(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "6"]):
            self.assertEqual(main.main(), 16)

    def test_steps_10(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "10"]):
            self.assertEqual(main.main(), 50)

    def test_steps_50(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "50"]):
            self.assertEqual(main.main(), 1594)

    def test_steps_100(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "100"]):
            self.assertEqual(main.main(), 6536)                