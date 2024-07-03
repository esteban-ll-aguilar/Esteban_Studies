from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan

class GraphLabeled(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        for i in range(0, num_vert):
            self.__labels.append(nan)
            
    def setLabel(self, vertex, label):
        self.__labels[vertex] = label
        
    def getLabel(self, vertex):
        return self.__labels[vertex]
    
    
