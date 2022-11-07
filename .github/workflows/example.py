import unittest
import dotesta


class TestStringMethods(unittest.TestCase):    
    def test_suma3(self):
        result = dotesta.suma3(10, 2, 3)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
