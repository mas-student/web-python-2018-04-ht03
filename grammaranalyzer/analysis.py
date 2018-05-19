from nltk import pos_tag

from .parse import split_snake_case_name_to_words


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    result = pos_info[0][1] in ['VB', 'VBZ', 'VBP']
    return result

def starts_with_verb(name):
    return is_verb(list(split_snake_case_name_to_words(name))[0])

def not_starts_with_verb(name):
    return not starts_with_verb(name)
