import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test(self):
        with patch("sys.argv", ["", "", "example.txt"]):
            self.assertEqual(main.main(), 54)         