import graphviz


f = open('advent25_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

graph_nodes = {}
for line in lines:
    source, toks = line.split(': ')
    dests = toks.split()
    graph_nodes[source] = dests

g = graphviz.Graph(comment='Wire Graph')

for source, dests in graph_nodes.items():
    g.node(source)
    for dest in dests:
        g.edge(source, dest)


output_file_path = "advent25_graph"
g.render(output_file_path, format='png', cleanup=True, view=True)
