import fizzbuzz
import unittest

class TestCase(unittest.TestCase):
    def testfizz(self):
        self.assertEqual(fizzbuzz.fizz(3),"Fizz")

if __name__ == '__main__':
    unittest.main(verbosity=2)