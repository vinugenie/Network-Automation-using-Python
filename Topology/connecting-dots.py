import networkx as nx
import matplotlib.pyplot as plt
import json

def draw_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    print("All Nodes: {0}".format(nodes))
    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)

    # show graph
    plt.show()

topo = json.load(open("network.json"))
# print(topo)
graph = []
for node in topo:
    local = node["host"]
    for conn in node["connections"]:
        remote = conn["remote-host"]
        graph.append((local, remote))

print(graph)
draw_graph(graph)
