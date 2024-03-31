import unittest

from dict2 import Dict2, DictKeyNotFoundError

class TestDict2(unittest.TestCase):
    def setUp(self):
        self.obj = Dict2()
        self.obj['a'] = 1
        self.obj['b'] = 2
        self.obj['c'] = 3

    def test_get_existing_key(self):
        self.assertEqual(self.obj['a'], 1)
        self.assertEqual(self.obj['b'], 2)
        self.assertEqual(self.obj['c'], 3)

    def test_get_non_existing_key(self):
        with self.assertRaises(DictKeyNotFoundError):
            _ = self.obj['d']

    def test_set_key(self):
        self.obj['d'] = 4
        self.assertEqual(self.obj['d'], 4)

    def test_iterate_keys(self):
        keys = list(self.obj)
        self.assertEqual(keys, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()
