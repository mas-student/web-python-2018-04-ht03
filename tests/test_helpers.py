import unittest

from grammaranalyzer.helpers import is_true, is_not_dunder


class TestHelpers(unittest.TestCase):

    def test_is_true(self):
        self.assertEqual(is_true(''), False, '"" is not true')
        self.assertEqual(is_true('not empty string'), True, '"not empty string" is true')

    def is_not_dunder(self):
        self.assertEqual(is_not_dunder('value'), True)
        self.assertEqual(is_not_dunder('__value'), True)
        self.assertEqual(is_not_dunder('value__'), True)
        self.assertEqual(is_not_dunder('__value__'), False)


if __name__ == '__main__':
    unittest.main()
