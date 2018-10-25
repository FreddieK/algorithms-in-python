import random


class RandomContraction:
    minimumCut = None

    def __init__(self, list_, num_iterations=100):
        self.list_ = list_
        self.num_iterations = num_iterations

    def _get_lists(self):
        # Fetches original lists and removes duplicated edges, e.g. (0, 3) and
        # (3, 0)
        vertices = [x[0] for x in self.list_]
        edges = [[x[0], a] for x in self.list_ for a in x[1:]]
        edges_deduplicated = []
        for edge in edges:
            if not edge[::-1] in edges_deduplicated:
                edges_deduplicated.append(edge)
        return vertices, edges_deduplicated

    @staticmethod
    def _contract_edges(edge, head, tail):
        # Update all edges pointing to the head vertex
        # of the selected edge to instead point at the tail
        if edge[0] == head:
            edge[0] = tail
        if edge[1] == head:
            edge[1] = tail
        return edge

    @staticmethod
    def _contract_graph(vertices, edges):
        edge = random.choice(edges)
        tail, head = edge[0], edge[1]
        edges.remove(edge)
        edges = [RandomContraction._contract_edges(edge, head, tail)
                 for edge in edges]
        edges = [x for x in edges if not x[0] == x[1]]
        vertices.remove(head)
        return vertices, edges

    def run(self):
        for index in range(0, self.num_iterations):
            if index % 10 == 0:
                print(f'Iteration: {index}')
            random.seed(index)
            vertices, edges = self._get_lists()
            random.seed(index)
            while len(vertices) > 2:
                vertices, edges = self._contract_graph(vertices, edges)
            if (self.minimumCut is None) or len(edges) < self.minimumCut:
                self.minimumCut = len(edges)
                print(f'{len(edges)} - new low!')
