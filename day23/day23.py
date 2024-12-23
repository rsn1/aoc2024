from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

graph = defaultdict(list)
nodes = []
#create graph
for edge in data:
    n1, n2 = edge.split('-')
    graph[n1].append(n2)
    graph[n2].append(n1)
    if n1 not in nodes:
        nodes.append(n1)
    if n2 not in nodes:
        nodes.append(n2)

count = 0
visited = set() #(n1,n2,n3)
for node in graph:
    lanset = set()
    neighbours = graph[node]
    for ne in neighbours:
        nn = graph[ne]
        in_common = list(set(neighbours).intersection(nn))
        for k in in_common:
            if k[0] == 't' or node[0] == 't' or ne[0] == 't':
                lanset.add(frozenset((node,ne,k)))
    visited = visited.union(lanset)

print(len(visited))
