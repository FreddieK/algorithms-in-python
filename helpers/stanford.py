
def read_file(filename):
    path = f'data/{filename}'
    with open(path) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]
