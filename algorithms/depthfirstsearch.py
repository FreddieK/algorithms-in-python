import pandas as pd


class DepthFirstSearch:
    _current_leader = None
    _iteration = None

    def __init__(self, edges):
        self.edges = edges
        self.vertices = list(set([x for sublist in edges for x in sublist]))
        self.current_label = len(self.vertices)
        self.explored = set()
        self.finishing_order = {}
        self.vertix_groups = {}

    def _dfs(self, vertix, reverse=False):
        self.explored.add(vertix)
        tail, head = 0, 1
        if reverse:
            tail, head = head, tail
        children = [x[head] for x in self.edges if x[tail] == vertix]
        for child in children:
            if child not in self.explored:
                self._dfs(child, reverse)

        if self._iteration == 'first':
            self.finishing_order[vertix] = self.current_label
            self.current_label -= 1
        elif self._iteration == 'second':
            self.vertix_groups[vertix] = self._current_leader

        print(len(self.explored)/len(self.vertices))

    def first_pass(self):
        self._iteration = 'first'
        self.current_label = len(self.vertices)
        vertices = self.vertices

        self.explored = set()
        for vertix in vertices:
            print(f'Continuing for vertix {vertix}')
            print(f'Explored: {self.explored}')
            if vertix not in self.explored:
                self._dfs(vertix, True)

    def second_pass(self):
        print('Second pass')
        self._iteration = 'second'
        run_order = sorted(self.finishing_order.items(), key=lambda x: x[1])
        vertices = [x[0] for x in run_order]

        self.explored = set()
        for vertix in vertices:
            print(f'Continuing for vertix {vertix}')
            if vertix not in self.explored:
                self._current_leader = vertix
                self._dfs(vertix, False)

    def get_scc_sizes(self):
        scc = [x for x in self.vertix_groups.values()]
        return pd.Series(scc).value_counts()
