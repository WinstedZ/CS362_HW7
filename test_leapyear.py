import leapyear
import unittest

class TestCase(unittest.TestCase):
    def testfourhundred(self):
        self.assertEqual(leapyear.fourhundred(400),"Is a leap year")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)