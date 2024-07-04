from controls.tda.graph.graphLabeledManaged import GraphLabeledManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan

class GraphLabeledNoManaged(GraphLabeledManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertex = {}
        for i in range(0, num_vert):
            self.__labels.append(nan)
            
        
            
    def insert_edges_weigth_E(self, label1, label2, weigth):
        v = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v != -1 and v2 != -1:
            self.insert_edges_weigth(v, v2, weigth)
            self.insert_edges_weigth(v2, v, weigth) 
        else:
            raise ArrayPositionException("No existen los vertices")