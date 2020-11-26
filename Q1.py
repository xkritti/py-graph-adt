from graph import Graph

g = Graph()
for i in range(6):
    g.addVertex(chr(ord("A")+i))
g.addEdge("A","B",1)
g.addEdge("A","D",3)
g.addEdge("B","C",6)
g.addEdge("B","D",5)
g.addEdge("B","E",1)
g.addEdge("C","E",5)
g.addEdge("C","F",2)
g.addEdge("D","E",1)
g.addEdge("E","F",4)


for v in g :
    for w in v.getConnections():
        temp_w = v.connectedTo
        w_id = w.getId()
        for tx in temp_w:
            txx = tx.getId()
            if txx == w_id :
                print("(%s,%s,%s)"% (v.getId(),w.getId(),v.getWeight(tx)))