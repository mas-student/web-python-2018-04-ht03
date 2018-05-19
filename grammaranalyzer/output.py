import sys
import json

def to_file(file, lines):
    file.writelines([line + '\n' for line in lines])

def to_fuzzy(records):
    lines = ['word "{}" found {} times'.format(*record) for record in records]
    return '\n'.join(lines)

def to_csv(records):
    lines = [','.join(map(str, record)) for record in records]
    return '\n'.join(lines)

def to_json(records):
    return json.dumps(records)

def to_output(output, buffer):
    if output == '-':
        sys.stdout.write(buffer)
    else:
        with open(output, 'wt') as f:
            f.write(buffer)
