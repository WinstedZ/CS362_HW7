import fizzbuzz
import unittest

class TestCase(unittest.TestCase):
    def testfizz(self):
        self.assertEqual(fizzbuzz.fizz(3),"Fizz")

    def testbuzz(self):
        self.assertEqual(fizzbuzz.fizz(5),"Buzz")

    def testfizzbuzz(self):
        self.assertEqual(fizzbuzz.fizz(15),"FizzBuzz")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)