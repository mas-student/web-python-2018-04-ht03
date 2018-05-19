import sys
import click


from grammaranalyzer.core import explore_projects, normalize_format


@click.command()
@click.argument('projects', nargs=-1)
@click.option('--root', help='The path to find projects.', default='.')
@click.option('--language', help='The language of file to filter.', default='python')
@click.option('--node', help='The type of node to filter.', default='function')
@click.option('--pos', help='The part of speech to filter.', default='verb')
@click.option('--limit', help='The count limit for filter.', default=10)
@click.option('--output', help='The filename to output.', default='-')
@click.option('--format', help='The format to output.')
def main(projects, root, language, node, pos, limit, output, format):
    output, format = normalize_format(output, format)

    status = 1
    if len(projects) == 0:
        print('No project has been given'.format())
    elif language not in ['python']:
        print('The language "{}" is not supported. Try {}.'.format(language, ['python']))
    elif node not in ['function', 'variable']:
        print('The node "{}" is not supported'.format(pos, ['function', 'variable']))
    elif pos not in ['verb']:
        print('The part of speech "{}" is not supported'.format(pos, ['verb']))
    elif format not in ['csv', 'json', 'fuzzy']:
        print('The format "{}" is not supported'.format(format, ['csv', 'json', 'fuzzy']))
    else:
        status = 0

    if status != 0:
        sys.exit(status)

    explore_projects(projects, root, language, node, pos, int(limit), output, format)


if __name__ == "__main__":
    main()
