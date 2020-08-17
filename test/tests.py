import unittest

import code

class TestMethods(unittest.TestCase):
    def test_answer():
    	assert code.inc(3) == 4

if __name__ == '__main__':
    unittest.main() 