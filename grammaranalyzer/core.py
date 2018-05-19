import os
import git
import collections
from operator import itemgetter

from .helpers import is_python, get_filenames_from_path
from .parse import get_nodes_from_filenames, get_node_name, get_words_from_names, is_function_node, is_name_node
from .analysis import is_verb
from .output import to_fuzzy, to_csv, to_json, to_output


def get_words_from_path(path, language, node, pos):
    language_filter = None
    node_filter = None
    pos_filter = None
    if language == 'python':
        language_filter = is_python
    if node == 'function':
        node_filter = is_function_node
    elif node == 'variable':
        node_filter = is_name_node
    if pos == 'verb':
        pos_filter = is_verb

    filenames = filter(language_filter, get_filenames_from_path(path))
    nodes = filter(node_filter, get_nodes_from_filenames(filenames))
    node_names = map(get_node_name, nodes)
    words = filter(pos_filter, get_words_from_names(node_names))

    return words

def get_occurrences_from_path(path, language, node, pos, limit):
    verbs = list(get_words_from_path(path, language, node, pos))
    occurrences = collections.Counter(verbs).most_common(limit)
    return occurrences

def fetch_project(projects_path, project_uri):
    if project_uri.startswith('git@github.com'):
        project_name = project_uri.split('/')[1].split('.')[0]
        project_path = os.path.join(projects_path, project_name)
        if not os.path.exists(project_path):
            git.Git(projects_path).clone(project_uri)

    else:
        project_path = os.path.join(projects_path, project_uri)

    return project_path

def to_format(format, occurrences):
    if format == 'csv':
        return to_csv(occurrences)
    elif format == 'json':
        return to_json(occurrences)
    elif format == 'fuzzy':
        return to_fuzzy(occurrences)

    return to_fuzzy(occurrences)

def normalize_format(output, format):
    if format is None:
        if output.endswith('.csv'):
            return output, 'csv'
        elif output.endswith('.json'):
            return output, 'json'
        else:
            return output, 'fuzzy'

    return output, format

def explore_projects(projects, projects_path, language, node, pos, limit, output, format):
    total_counter = collections.Counter()
    total_top_verbs = []
    for project in projects:
        path = fetch_project(projects_path, project)

        occurrences = list(get_occurrences_from_path(path, language, node, pos, limit))

        buffer = to_format(format, occurrences)
        to_output(output, buffer)

        total_counter.update(dict(occurrences))
        total_top_verbs += map(itemgetter(0), occurrences)
