import numpy as np
import networkx as nx

links = np.loadtxt(".gitignore/links.txt", delimiter='\t', dtype=int)
nicknames = np.loadtxt(".gitignore/nicknames.txt", delimiter='\t', dtype=str)

nodes = []
for i,j in nicknames:
    nodes.append(int(i))

edges = []
for k,l in links:
    edge = (k,l)
    edges.append(edge)

Graph = nx.DiGraph()
Graph.add_nodes_from(nodes)
Graph.add_edges_from(edges)

#Adjacency Matrix
#adjacency_matrix = nx.to_numpy_matrix(Graph)

#Adjacency List
adjacency_list = nx.to_dict_of_lists(Graph)

#How many steps would it take to reach Mr.Shimazu(23) from me(21)?
def BFS(Start, Goal):
    Q = []
    Checked = set()

    for i in adjacency_list[Start]:
        Q.append((i, 1))
        Checked.add(i)
    print("Original Q: " + str(Q))

    while len(Q) > 0:
        if Q[0][0] == Goal:
            print(Q[0][1])
            break
        else:
            for k in adjacency_list[Q[0][0]]:
                if k not in Checked:
                    Q.append((k, Q[0][1] + 1))
            Q.pop(0) 


        
BFS(0, 16)


