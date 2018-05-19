import unittest
import ast

from grammaranalyzer.parse import \
    get_tree_from_content, get_nodes_from_trees, get_node_id, split_snake_case_name_to_words, \
    is_function_node, is_name_node, get_node_name


class TestParse(unittest.TestCase):

    @staticmethod
    def _nodes2names(nodes):
        return list(map(get_node_id, filter(is_name_node, nodes)))

    def test_get_nodes_from_trees(self):
        trees = [get_tree_from_content('a = 1\nb = 17')]

        names = self._nodes2names(get_nodes_from_trees(trees))

        self.assertEqual(names, ['a', 'b'])

    def test_is_name_node(self):
        trees = [get_tree_from_content('a = 1\nb = 17')]

        self.assertEqual(is_name_node(list(ast.walk(ast.parse('a = 1')))[2]), True)

    def test_get_name_node(self):
        self.assertEqual(get_node_name(list(ast.walk(ast.parse('a = 1')))[2]), 'a')
        self.assertEqual(get_node_name(list(ast.walk(ast.parse('def f(): pass')))[1]), 'f')

    def test_split_snake_case_name_to_words(self):
        self.assertEqual(list(split_snake_case_name_to_words('left_right')), ['left', 'right'])
        self.assertEqual(list(split_snake_case_name_to_words('getValue')), ['getValue'])
        self.assertEqual(list(split_snake_case_name_to_words('__do_it__')), ['do', 'it'])


if __name__ == '__main__':
    unittest.main()
