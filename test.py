import unittest 
from main import to_upper

class TestCase(unittest.TestCase):
    def test_to_upper(self):
        name = 'Rishta'
        upper_name = to_upper(name)
        self.assertEqual(upper_name,"RISHTA")

if __name__=='__main__':
    unittest.main()