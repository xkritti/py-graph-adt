import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['BKK','HKG','NRT','YVR','LAX','ICN','SIN'])
G.add_weighted_edges_from([("BKK","HKG",1000),
("BKK","NRT",3000),
("BKK","ICN",2250),
("BKK","SIN",1000),
("HKG","NRT",2000),
("HKG","YVR",6500),
("HKG","LAX",7250),
("NRT","YVR",4500),
("NRT","LAX",5500),
("YVR","ICN",5000),
("LAX","ICN",6000),
])
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw_shell(G,with_labels = True,font_weight='bold',edge_color="red")
# save pix
# plt.savefig("graphQ2.png")
plt.show()