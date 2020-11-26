import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['A','B','C','D','E','F'])
G.add_weighted_edges_from([("A","B",1),
("A","D",3), 
("B","C",6), 
("B","D",5), 
("B","E",1), 
("C","E",5),
("C","F",2), 
("D","E",1), 
("E","F",4)])

labels = {("A","B"):1, 
("A","D"):3,
("B","C"):6, 
("B","D"):5, 
("B","E"):1, 
("C","E"):5, 
("C","F"):2, 
("D","E"):1, 
("E","F"):4}
pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=edge_labels)

nx.draw_circular(G,with_labels = True,font_weight='bold')
# save pix
# plt.savefig("graphQ2.png")
plt.text(-0.4, 1, r'Simple Graph Display', fontsize=10)
plt.show()