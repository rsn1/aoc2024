import networkx as nx

with open("input.txt") as f:
    data = f.read().splitlines()

G = nx.Graph()

for edge in data:
    node1, node2 = edge.split('-')
    G.add_edge(node1,node2)

maxclique = max(nx.find_cliques(G),key=len)
maxclique.sort()
print(",".join(maxclique))
