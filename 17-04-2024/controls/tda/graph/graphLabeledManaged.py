from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan

class GraphLabeledManaged(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        self.__labels = []
        self.__labelsVertex = {}
        for i in range(0, num_vert):
            self.__labels.append(nan)
            
            
    def getVertex(self, label):
        try:
            return self.__labelsVertex[str(label)]
        except:
            return -1
        
        
        
    def getVertexAux(self, label):
        id = -1
        for i in range(0, self.num_vertex):
            print(str(self.__labels[i]) + " == " + str(label))
            if str(self.__labels[i]) == str(label):
                id = i
                break
        return id
    
    def labelVertex(self, vertex, label):
        self.__labels[vertex] = label
        self.__labelsVertex[str(label)] = vertex
        print(self.__labelsVertex)
        
    def getLabel(self, vertex):
        return self.__labels[vertex]
    
    def exist_edges_E(self, label1, label2):
        v = self.getVertex(label1)
        v2 = self.getVertex(label2)
        
        if v != -1 and v2 != -1:
            return self.exist_edges(v, v2)
        return False
    
    def insert_edges_weigth_E(self, label1, label2, weigth):
        v = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v != -1 and v2 != -1:
            return self.insert_edges_weigth(v, v2, weigth)
        raise ArrayPositionException("No se encontro el vertice")
    
    def insert_edges_E(self, label1, label2):
        self.insert_edges_weigth_E(label1, label2, nan)
    
    def weigth_edges_E(self, label1, label2):
        v = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v != -1 and v2 != -1:
            return self.weigth_edges(v, v2)
        raise ArrayPositionException("No se encontro el vertice")
    
    def adjacent_E(self, label):
        v = self.getVertex(label)
        if v != -1:
            return self.adjacent(v)
        raise ArrayPositionException("No se encontro el vertice")
    
    
    
    
    
#python -m pydoct -w Esteban_Studies/17-04-2024/controls/tda/graph/graphLabeled.py