
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
        return int(split[0]), int(split[1])

    cleaned_vertices = dict()
    for vertex in vertices:
        # Skip first last index to remove index vertex and newline character
        cleaned_vertices[int(vertex[0])] = [to_tuple(x) for x in vertex[1:-1]]
    return cleaned_vertices
