import unittest
from Functions4test import add


class testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,1), 3)
        self.assertNotEqual(add(2.1, 1.2), 5)
      

if __name__ == '__main__':
    unittest.main()
