
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


def read_weighted_graph_file(filename, split='\t'):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    vertices = [[x for x in line.split(split)] for line in content]

    def to_tuple(x):
        split = str.split(x, ',')
        if len(split) == 1:  # Initial vertex index
            return int(split[0])
        elif len(split) == 2:
            return int(split[0]), int(split[1])

    cleaned_vertices = []
    for vertex in vertices:
        # Skip last index to remove newline character
        cleaned_vertices.append([to_tuple(x) for x in vertex[:-1]])

    return cleaned_vertices
