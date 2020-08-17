import unittest

import src


class TestMethods(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(src.happy(), ":)")

    def test_sad(self):
    	self.assertEqual(src.sad(), ":(")


if __name__ == '__main__':
    unittest.main()