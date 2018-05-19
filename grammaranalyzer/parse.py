import ast

from .helpers import is_true, is_not_dunder, get_content_from_filename


def get_tree_from_content(content):
    try:
        return ast.parse(content)
    except SyntaxError as e:
        print(e), content

def get_tree_from_filename(filename, with_filenames=False, with_file_content=False):
    main_file_content = get_content_from_filename(filename)
    tree = get_tree_from_content(main_file_content)
    if with_filenames:
        if with_file_content:
            result = (filename, main_file_content, tree)
        else:
            result = (filename, tree)
    else:
        result = tree
    return result

def get_trees_from_filenames(filenames):
    for filename in filenames:
        element = get_tree_from_filename(filename)
        if element:
            yield element

def is_name_node(node):
    return isinstance(node, ast.Name)

def is_function_node(node):
    return isinstance(node, ast.FunctionDef)

def get_node_name(node):
    if is_name_node(node):
        return node.id
    elif is_function_node(node):
        return node.name.lower()

    return

def get_node_id(node):
    return node.id

def get_nodes_from_trees(trees):
    for nodes in map(ast.walk, trees):
        for node in nodes:
            if node:
                yield node

def get_nodes_from_filenames(filenames):
    return get_nodes_from_trees(get_trees_from_filenames(filenames))

def split_snake_case_name_to_words(name):
    return filter(is_true, name.split('_'))

def get_words_from_names(names, splitter=split_snake_case_name_to_words):
    for words in map(splitter, filter(is_not_dunder, names)):
        for word in words:
            yield word
