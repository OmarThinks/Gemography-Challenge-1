import unittest

class CircleCITestCase(unittest.TestCase):
    def test_001_test(self):
        self.assertEqual(1,1)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()