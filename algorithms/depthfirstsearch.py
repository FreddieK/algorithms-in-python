class DepthFirstSearch:

    def __init__(self, edges):
        self.edges = edges
        self.vertices = list(set([x for sublist in edges for x in sublist]))
        self.explored = []
        self.current_label = len(self.vertices)
        self.labels = {}

    def dfs(self, vertix, reverse=False):
        self.explored.append(vertix)
        tail, head = 0, 1
        if reverse:
            tail, head = head, tail
        children = [x[head] for x in self.edges if x[tail] == vertix]
        for child in children:
            if child not in self.explored:
                self.dfs(child, reverse)

        self.labels[vertix] = self.current_label
        self.current_label -= 1

    def dfs_loop(self):
        # Mark nodes unexplored
        # current_label = len(self.vertices)

        for vertix in self.vertices:
            if vertix not in self.explored:
                self.dfs(vertix)