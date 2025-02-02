hundred_mile_forest = {
    'A': {'B': 15, 'D': 10, 'G': 20},
    'B': {'A': 15, 'C': 25},
    'C': {'B': 25, 'E': 60, 'F': 75},
    'D': {'A': 10, 'E': 20},
    'E': {'D': 20, 'C': 60, 'J': 15, 'K': 20},
    'F': {'C': 75, 'K': 30},
    'G': {'A': 20, 'H': 15, 'I': 10, 'J': 25},
    'H': {},
    'I': {'G': 10, 'K': 15},
    'J': {'E': 15, 'K': 15},
    'K': {'I': 15, 'J': 15, 'E': 20, 'F': 30},
    }

def add_edge(graph, source, dest=None, weight=None):
    if source not in graph.keys():
        graph[source] = {}
    if source in graph.keys() and dest in graph[source].keys():
        return
    elif dest is not None and weight is not None:
        graph[source][dest] = weight

def find_biggest_weight(graph):
    max_weight = float('-inf')
    best_edge = None

    for source, neighbors in graph.items():
        for dest, weight in neighbors.items():
            if weight > max_weight:
                max_weight = weight
                best_edge = (source, dest, weight)

    return best_edge


def get_minimum(graph):
    min_weight = float('inf')
    min_edge = None

    for source, neighbors in graph.items():
        for dest, weight in neighbors.items():
            if weight < min_weight:
                min_weight = weight
                min_edge = (source, dest, weight)

    print(min_edge)
    del graph[min_edge[0]][min_edge[1]]

    return min_edge

def print_cheapest_way(costs_dict, parents_array):
    way_dict = {}
    paths = {}
    for d, c in costs_dict.items():
        way_dict[d] = c
        tmp_array = []
        current_d = d
        while parents_array[current_d]:
            tmp_array.append(current_d)
            current_d = parents_array[current_d]
        else:
            tmp_array.append(current_d)
            paths[d] = ''.join(reversed(tmp_array))
    print("DICTIONARY WAY", way_dict)
    print("BEST PATHS", paths)


def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None

    for name, cost in costs_dict.items():
        if name not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name

    return cheapest_key

def cheapest_way(graph, start_vertex):
    costs = {}
    parents = {}

    for name in graph.keys():
        costs[name] = float('inf')

    processed = []
    current_node = start_vertex
    costs[current_node] = 0
    parents[current_node] = None

    while current_node:
        for neighbour in graph[current_node]:
            if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
                costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
                parents[neighbour] = current_node

        processed.append(current_node)
        current_node = get_cheapest_node(costs, processed)

    print_cheapest_way(costs, parents)
    return costs, parents




V = {}
#
add_edge(V, "A", "B", 2)
add_edge(V, "A", "D", 4)
add_edge(V, "B", "C", 3)
add_edge(V, "B", "D", 3)
add_edge(V, "C", "E", 2)
add_edge(V, "D", "C", 3)
add_edge(V, "D", "E", 4)
add_edge(V, "E")

# cheapest_way(V, "A")
print('_'*30)
cheapest_way(hundred_mile_forest, 'A')
print('_'*30)
