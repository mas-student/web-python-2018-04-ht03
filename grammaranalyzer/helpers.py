import os


def is_true(value):
    return not not value

def is_not_dunder(name):
    return not (name.startswith('__') and name.endswith('__'))

def is_python(filename):
    return filename.endswith('.py')

def get_filenames_from_path(path):
    for dirname, dirs, files in os.walk(path, topdown=True):
        for filename in files:
            yield os.path.join(dirname, filename)

def get_content_from_filename(filename):
    with open(filename, 'r', encoding='utf8') as attempt_handler:
        return attempt_handler.read()
