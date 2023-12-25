import graphviz


f = open('advent20_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

graph_nodes = {}
for line in lines:
    parts = line[1:].split('->')
    source = parts[0].strip()
    dests = [s.strip() for s in parts[1].split(',')]
    graph_nodes[source] = dests

g = graphviz.Digraph(comment='Pulse Graph')

for source, dests in graph_nodes.items():
    g.node(source)
    for dest in dests:
        g.edge(source, dest)

output_file_path = "advent20_graph"
g.render(output_file_path, format='png', cleanup=True, view=True)
