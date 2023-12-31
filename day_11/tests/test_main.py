import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_expansion_2(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "2"]):
            self.assertEqual(main.main(), 374)    

    def test_expansion_10(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "10"]):
            self.assertEqual(main.main(), 1030)           

    def test_expansion_100(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "100"]):
            self.assertEqual(main.main(), 8410)              