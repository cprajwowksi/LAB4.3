import unittest

def suma3(a,b,c):
  result = a + b + c
  return result;
class TestStringMethods(unittest.TestCase):
    
    def test_suma3(self):
        result = suma3(10, 2, 3)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
