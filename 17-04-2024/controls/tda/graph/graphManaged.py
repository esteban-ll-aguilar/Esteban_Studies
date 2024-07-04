from controls.tda.graph.graph import Graph
from controls.tda.linked.linkedList import Linked_List
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan
class GraphManaged(Graph):
    def __init__(self, num_vert):
        super().__init__()
        self.__numVer = num_vert
        self.__numEdg = 0
        self.__listAdjacent =[]
        
        for i in range(0,num_vert):
            self.__listAdjacent.append(Linked_List())
            
    @property
    def num_vertex(self):
        return self.__numVer
    @property
    def num_edges(self):
        return self.__numEdg
    
    def setNumEdges(self, number):
        self.__numEdg = number
    
    def exist_edges(self, v1, v2):
        band = False
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arrayAdj = listAdj.toArray
                for i in range(0, listAdj._length):
                    adj = arrayAdj[i]
                    if adj._destination == v2:
                        band = True
        else:
            raise ArrayPositionException("Delimites out")
        return band
        
        
    def weigth_edges(self, v1, v2):
        weigth = None
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arrayAdj = listAdj.toArray
                for i in range(0, listAdj._length):
                    adj = arrayAdj[i]
                    if adj._destination == v2:
                        weigth = adj._weigth
                        break
        else:
            raise ArrayPositionException("Delimites out")
        return weigth
        
    def insert_edges_weigth(self, v1, v2, weigth):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exist_edges(v1, v2):
                self.__numEdg += 1
                adj = Adjacent()
                adj._destination = v2
                adj._weigth = weigth
                self.__listAdjacent[v1].add(adj, self.__listAdjacent[v1]._length)
        else:
            raise ArrayPositionException("Delimites out")
        
    def insert_edges(self, v1, v2):
        self.insert_edges_weigth(v1, v2, nan)
        
    def adjacent(self, v1):
        return self.__listAdjacent[v1]
    
    def addVertex(self):
        self.__numVer += 1
        self.__listAdjacent.append(Linked_List())
            
    