import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['A','B','C','D','E','F'])
G.add_weighted_edges_from([("A","B",1),("A","D",3), ("B","C",6), ("B","D",5), ("B","E",1), ("C","E",5),("C","F",2), ("D","E",1), ("E","F",4)])
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw_shell(G,with_labels = True,font_weight='bold')
# save pix
# plt.savefig("graphQ2.png")
plt.show()