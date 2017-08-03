import unittest
import Models

class BasicTestMethods(unittest.TestCase):
    def test_asdf(self):
        self.assertEqual(Models.asdf(), "asdf", 'nah')
        self.assertNotEqual(Models.asdf(), "asdf1", 'nah')
        #self.assertEqual(asdf(), "asdf1", 'nah')

if __name__ == '__main__':
    unittest.main()
