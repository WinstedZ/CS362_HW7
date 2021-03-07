import leapyear
import unittest

class TestCase(unittest.TestCase):
    def testfourhundred(self):
        self.assertEqual(leapyear.leap(400),"Is a leap year")
    
    def testonehundred(self):
        self.assertEqual(leapyear.leap(100),"Is not a leap year")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)