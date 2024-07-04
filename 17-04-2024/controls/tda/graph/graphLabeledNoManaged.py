from controls.tda.graph.graphNoManaged import GraphNoManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan

class GraphLabeledNoManaged(GraphNoManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertex = {}
        for i in range(0, num_vert):
            self.__labels.append(nan)
            
        