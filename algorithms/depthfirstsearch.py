import pandas as pd


class DepthFirstSearch:
    _current_leader = None
    _iteration = None

    def __init__(self, edges):
        self.edges = edges
        self.vertices = set([x for sublist in edges for x in sublist])
        self.current_label = len(self.vertices)
        self.explored = set()
        self.finishing_order = {}
        self.vertex_groups = {}

    def _dfs_recursive(self, vertex, reverse=False):
        # Ran into issues due to the amount of recursions needed, so replaced
        # with an iterative implementation.
        # Further, the look for children in the original edge list is too slow
        # when number of edges increases, to needs to be changed into an
        # adjacency list implementation (as now used in the iterative
        # implementation.
        #
        # @deprecated

        self.explored.add(vertex)
        tail, head = 0, 1
        if reverse:
            tail, head = head, tail
        children = [x[head] for x in self.edges if x[tail] == vertex]
        for child in children:
            if child not in self.explored:
                self._dfs(child, reverse)
        if self._iteration == 'first':
            self.finishing_order[vertex] = self.current_label
            self.current_label -= 1
        elif self._iteration == 'second':
            self.vertex_groups[vertex] = self._current_leader

    def _dfs(self, starting_vertex, adjacency_list):
        stack = [starting_vertex]
        while len(stack) > 0:
            vertex = stack.pop()
            self.explored.add(vertex)
            if vertex in adjacency_list.keys():
                children = [child for child in adjacency_list[vertex] if
                            child not in self.explored]
            else:
                children = []
            if len(children) > 0:
                stack.append(vertex)
                for child in children:
                    stack.append(child)
            else:
                if self._iteration == 'first':
                    self.finishing_order[vertex] = self.current_label
                    self.current_label -= 1
                elif self._iteration == 'second':
                    self.vertex_groups[vertex] = self._current_leader

    def first_pass(self):
        self._iteration = 'first'
        self.current_label = len(self.vertices)
        vertices = self.vertices

        reverse = True
        tail, head = 0, 1
        if reverse:
            tail, head = head, tail
        df = pd.DataFrame(self.edges)
        adjacency_list = df.groupby(tail)[head].apply(lambda x: x.tolist())

        self.explored = set()
        for vertex in vertices:
            if vertex not in self.explored:
                self._dfs(vertex, adjacency_list)

    def second_pass(self):
        self._iteration = 'second'
        run_order = sorted(self.finishing_order.items(), key=lambda x: x[1])
        vertices = [x[0] for x in run_order]

        reverse = False
        tail, head = 0, 1
        if reverse:
            tail, head = head, tail
        df = pd.DataFrame(self.edges)
        adjacency_list = df.groupby(tail)[head].apply(lambda x: x.tolist())

        self.explored = set()
        for vertex in vertices:
            if vertex not in self.explored:
                self._current_leader = vertex
                self._dfs(vertex, adjacency_list)

    def get_scc_sizes(self):
        scc = [x for x in self.vertex_groups.values()]
        return pd.Series(scc).value_counts()
