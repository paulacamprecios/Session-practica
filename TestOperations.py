#I will use unittest
from Operations import *
import unittest

class Test_Sum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)

if __name__ == "__main__":
    unittest.main()