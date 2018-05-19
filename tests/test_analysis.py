import unittest

from grammaranalyzer.analysis import is_verb


class TestAnalysis(unittest.TestCase):

    def test_is_verb(self):
        self.assertEqual(is_verb('do'), True)
        self.assertEqual(is_verb('hello'), False)


if __name__ == '__main__':
    unittest.main()
