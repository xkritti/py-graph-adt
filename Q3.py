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
labels = {("BKK","HKG"):1000, 
("BKK","NRT"):3000,
("BKK","ICN"):2250, 
("BKK","SIN"):1000, 
("HKG","NRT"):2000, 
("HKG","YVR"):6500, 
("HKG","LAX"):7250, 
("NRT","YVR"):4500, 
("NRT","LAX"):5500, 
("YVR","ICN"):5000, 
("LAX","ICN"):6000, }
pos = nx.circular_layout(G)
nx.draw_circular(G,with_labels=True,edge_color='red')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=edge_labels)
# save pix
# plt.savefig("graphQ2.png")
plt.text(0, 1, r'Routes and Distances (miles)', fontsize=15)
plt.show()