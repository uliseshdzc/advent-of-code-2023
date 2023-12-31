import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_part_1(self):
        with patch("sys.argv", ["", "data\\example.txt", "1", "7", "27"]):
            self.assertEqual(main.main(), 2)

    def test_part_2(self):
        with patch("sys.argv", ["", "data\\example.txt", "2"]):
            self.assertEqual(main.main(), 47)
          