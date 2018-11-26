import operator


def read_file(filename='edges.txt'):
    """
    :param filename: Optional parameter if filename would be changed
    :return: Tuple of metadata (nr of nodes and edges, and then actual list
    """
    path = f'data/{filename}'
    with open(path) as f:
        read_data = f.read()
    lines = [x for x in read_data.split('\n')]
    metadata = [int(x) for x in lines[0].split()]
    # Shaving of last item in list as it is an empty line
    list_ = [[int(item) for item in line.split()] for line in lines[1:-1]]

    return metadata, list_


class PrimsMST:
    """
    Your task is to run Prim's minimum spanning tree algorithm on this graph.

    You should report the overall cost of a minimum spanning tree --- an
    integer, which may or may not be negative --- in the box below.
    """

    def __init__(self, num_vertices, edges, initial_vertex=1):
        self.num_vertices = num_vertices

        # treat edges like directed
        edges_reversed = [[x[1], x[0], x[2]] for x in edges]
        self.edges = edges + edges_reversed

        self.spanning_tree = set([initial_vertex])
        self.edge_costs = []

    def _find_best_edge(self):
        edges_to_explore = [edge for edge in self.edges if edge[0] in
                            self.spanning_tree and edge[1] not in
                            self.spanning_tree]
        sorted_edges_to_explore = sorted(edges_to_explore,
                                         key=operator.itemgetter(2))
        next_edge = sorted_edges_to_explore[0]
        self.spanning_tree.add(next_edge[1])
        self.edge_costs.append(next_edge[2])

        return next_edge

    def find_mst(self):
        while len(self.spanning_tree) < self.num_vertices:
            self._find_best_edge()
        return self.spanning_tree, sum(self.edge_costs)