from django.test import SimpleTestCase

from  app import calc

class CalcTests(SimpleTestCase):
    def test_add_number(self):
        res =calc.add(5,6)
        
        self.assertEqual(res,11)
        
    def test_subtract_number(self):
        # test subtractiong numbers. 
        res =calc.subtract(10,15)
        
        self.assertEqual(res,5)
        