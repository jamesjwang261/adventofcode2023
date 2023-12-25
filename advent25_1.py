# used a quick graphviz visualisation to check out the structure of the graph
# because we have two approximately equal sized components,
# i decided an 'approximate' solution would probably work

# i know about minimum cuts but have never tried implementing them
# (and i didn't have access to networkx api at the time)
# so instead i tried using shortest path centrality

# idea: for any shortest path from a node in one component to the other,
# it will contain one of the 3 edges
# so if we take a large random sample of nodes and find their shortest paths,
# the most commonly seen edges should be these 3 edges


from collections import defaultdict, deque, Counter
import random


f = open('advent25_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]


graph_nodes = defaultdict(list)

for line in lines:
    source, toks = line.split(': ')
    dests = toks.split()
    graph_nodes[source].extend(dests)
    for dest in dests:
        graph_nodes[dest].append(source)


def shortest_path(graph, node1, node2):
    # bfs to find shortest path
    queue = deque([(node1, [])])  # (cur, edges in path)
    visited = set()

    while queue:
        cur, edges = queue.popleft()

        if cur == node2:
            return edges

        if cur not in visited:
            visited.add(cur)

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    queue.append((neighbor, edges + [(cur, neighbor)]))

    # If no path is found
    return None


N = 10000
random_pairs = random.choices(list(graph_nodes.keys()), k=2*N)
pairs = [(random_pairs[i], random_pairs[i + 1]) for i in range(0, 2*N, 2)]


path_edges = []
for n1, n2 in pairs:
    new_path = shortest_path(graph_nodes, n1, n2)
    if new_path:
        path_edges.extend(new_path)

edge_counts = Counter(path_edges)

# combine counts for directed edges (a -> b) and (b -> a) into (a -> b)
for (a, b) in edge_counts.copy():
    if b > a:
        edge_counts[(b, a)] += edge_counts[(a, b)]
        del edge_counts[(a, b)]

bad_edges = [s[0] for s in edge_counts.most_common(3)]


for a, b in bad_edges:
    graph_nodes[a].remove(b)
    graph_nodes[b].remove(a)


def connected_component_size(graph, start):
    visited = set()
    stack = [start]
    component_size = 0

    while stack:
        cur = stack.pop()

        if cur not in visited:
            visited.add(cur)
            component_size += 1

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return component_size

n1 = connected_component_size(graph_nodes, bad_edges[0][0])
n2 = connected_component_size(graph_nodes, bad_edges[0][1])
print(n1 * n2)
