import unittest
from sys import path
path.append('./src')
from rest_in_peace import Server

class TestDatabase(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
