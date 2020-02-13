import unittest

def enlarge(n):
    return 100*n

class TestEnlarge(unittest.TestCase):

    def test_results(self):
        self.assertEqual(enlarge(4), 400)

if __name__ == "__main__":
    unittest.main()
