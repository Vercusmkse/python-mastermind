import unittest
from mastermind import compare_codes

class TestCompareCodesFunction(unittest.TestCase):
    def test_perfect_match(self):
        self.assertEqual(compare_codes("RGBR", "RGBR"), (4, 0))

    def test_no_match(self):
        self.assertEqual(compare_codes("RGBR", "YMCY"), (0, 0))

    def test_partial_match(self):
        self.assertEqual(compare_codes("RGBR", "RGYR"), (3, 0))

    def test_partial_match_2(self):
        self.assertEqual(compare_codes("RGBR", "RBYG"), (1, 2))

    def test_same_color(self):
        self.assertEqual(compare_codes("RRRR", "RRRR"), (4, 0))

    def test_same_color_partial(self):
        self.assertEqual(compare_codes("RRRR", "RBBR"), (2, 0))

if __name__ == "__main__":
    unittest.main()
