from controls.tda.graph.graphNoManaged import GraphNoManaged
import numpy as np
class DijktraAlgorithm:
    def __init__(self, graph: object = None, start: int = 0, end: int = 0):
        self.__graph = graph
        self.__start = start-1 if start > 0 else 0
        self.__end = end-1 if end > 0 else 0
        self.__visited = [False] * self.__graph.num_vertex
        self.__distance = [np.inf] * self.__graph.num_vertex
        self.__parent = [-1] * self.__graph.num_vertex
        
        
    def __minDistance(self):
        min = np.inf
        min_index = -1
        for i in range(0, self.__graph.num_vertex):
            if self.__visited[i] == False and self.__distance[i] <= min:
                min = self.__distance[i]
                min_index = i
        return min_index
    
            
    def __printPath__(self):
        crawl = self.__end
        camino = []
        while (self.__parent[crawl] != -1):
            camino.append(crawl+1)
            crawl = self.__parent[crawl]
        camino.append(self.__start+1)
        camino = " -> ".join(map(str, camino[::-1]))
        
        print("Camino minimo entre: " + str(self.__start+1) + " y " + str(self.__end+1))
        print("Distancia: " + str(self.__distance[self.__end]))
        print("Camino: ", camino)
        print("Vertex \t\t Distance")
        for i in range(0, self.__graph.num_vertex):
            print(str(i+1) + " \t\t " + str(self.__distance[i]))
        
            
    @property
    def dijktra(self):
        self.__distance[self.__start] = 0
        for i in range(0, self.__graph.num_vertex):
            u = self.__minDistance()
            self.__visited[u] = True
            for v in range(0, self.__graph.num_vertex):
                if self.__visited[v] == False and self.__graph.exist_edges(u, v) and self.__distance[u] + self.__graph.weigth_edges(u, v) < self.__distance[v]:
                    self.__distance[v] = self.__distance[u] + self.__graph.weigth_edges(u, v)
                    self.__parent[v] = u
        self.__printPath__()
        return self.__distance[self.__end]


    