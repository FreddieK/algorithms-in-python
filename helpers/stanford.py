
def read_file(filename):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def read_graph_file(filename):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return [[int(x) for x in line.split('\t') if x.isdigit()]
            for line in content]