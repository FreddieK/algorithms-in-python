
def read_file(filename):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_graph_file(filename, split='\t'):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return [[int(x) for x in line.split(split) if x.isdigit()]
            for line in content]