from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
import numpy as np
#algoritmo obtenido del ejemplo en c++
#https://www.programiz.com/dsa/floyd-warshall-algorithm
class FloydWarshallAlgorithm:
    def __init__(self, graph:object=None, start:int=0, end:int=0):
        self.__graph = GraphLabeledNoManaged(0) if graph == None else graph
        self.__matrix = np.zeros((self.__graph.num_vertex, self.__graph.num_vertex))
        self.__matrixParent = np.zeros((self.__graph.num_vertex, self.__graph.num_vertex))
        self.__matrixParent.fill(-1)
        self.__start = start-1 if start > 0 else 0
        self.__end = end-1 if end > 0 else 0
            
    @property        
    def initMatrix(self):
        for i in range(0, self.__graph.num_vertex):
            for j in range(0, self.__graph.num_vertex):
                if i == j:
                    self.__matrix[i][j] = 0
                elif self.__graph.exist_edges(i, j):
                    self.__matrix[i][j] = self.__graph.weigth_edges(i, j)
                else:
                    self.__matrix[i][j] = np.inf
    
    @property
    def floydWarshall(self):
        self.initMatrix
        for k in range(0, self.__graph.num_vertex):
            for i in range(0, self.__graph.num_vertex):
                for j in range(0, self.__graph.num_vertex):
                    if self.__matrix[i][k] + self.__matrix[k][j] < self.__matrix[i][j]:
                        self.__matrix[i][j] = self.__matrix[i][k] + self.__matrix[k][j]
                        self.__matrixParent[i][j] = k
        self.__printPath__()
        return self.__matrix
        
    @property
    def __reconstruct_camino_mas_corto(self):
        camino = []
        start = self.__start
        end = self.__end
        
        if self.__matrix[start][end] == np.inf:
            return camino
        camino.append(start+1)
        while self.__matrixParent[start][end] != -1:
            start = int(self.__matrixParent[start][end])
            camino.append(start+1)
        camino.append(self.__end+1)
        camino = " -> ".join(map(str, camino))
        return camino
    
            
    def __printPath__(self):
        print("Camino minimo entre: " + str(self.__start+1) + " y " + str(self.__end+1))
        print("Distancia: " + str(self.__matrix[self.__start][self.__end]))
        print("Camino: ", self.__reconstruct_camino_mas_corto)
        print("Vertex \t\t Distance")
        for i in range(0, self.__graph.num_vertex):
            print(str(i+1) + " \t\t " + str(self.__matrix[self.__start][i]))
        
    
    
    
    
    