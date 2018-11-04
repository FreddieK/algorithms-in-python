
class GraphNotConnected(Exception):
    """Raised if there are no edges left to explore but there still exists
    unexplored vertices."""


def dijkstras_shortest_path(graph, starting_vertex):
    explored = set()
    min_cost = dict()
    explored.add(starting_vertex)
    min_cost[starting_vertex] = 0
    while len(explored) < len(graph):
        try:
            vertex, cost = explore_vertex(graph, explored, min_cost)
            explored.add(vertex)
            min_cost[vertex] = cost
        except GraphNotConnected:
            non_connected_vertices = set(graph.keys()) - explored
            for vertex in non_connected_vertices:
                explored.add(vertex)
                min_cost[vertex] = 1000000
    return min_cost


def explore_vertex(graph, explored, min_cost):
    vertices, costs = calculate_costs(graph, explored, min_cost)
    if len(vertices) == 0:
        raise GraphNotConnected()
    min_index = costs.index(min(costs))  # first index will suffice for ties
    return vertices[min_index], costs[min_index]


def calculate_costs(graph, explored, min_cost):
    vertices, costs = [], []
    for vertex in explored:
        for edge in graph[vertex]:
            if edge[0] not in explored:
                vertices.append(edge[0])
                costs.append(min_cost[vertex] + edge[1])
    return vertices, costs
