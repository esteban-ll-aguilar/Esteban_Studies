import numpy as np

class FloydWarshallAlgorithm:
    def __init__(self, graph: object = None,  start: int = 0, end: int = 0):
        self.__graph = graph
        self.__start = end - 1 if end > 0 else 0
        self.__end = start - 1 if start > 0 else 0
        self.__matrix = np.full((self.__graph.num_vertex, self.__graph.num_vertex), np.inf)
        self.__distance = np.full((self.__graph.num_vertex, self.__graph.num_vertex), -1)
        self.__parent = np.full((self.__graph.num_vertex, self.__graph.num_vertex), -1)
        self.__camino = None
        
        if self.__graph.allVertexConnected == False:
            raise Exception("No se puede realizar el algoritmo debido a que no todos los vertices estan conectados")
        if self.__start < 0 or self.__start >= self.__graph.num_vertex or self.__end < 0 or self.__end >= self.__graph.num_vertex:
            raise Exception("No se puede realizar el algoritmo debido a que los vertices no existen")
    
    @property
    def initMatrix(self):
        for i in range(self.__graph.num_vertex):
            for j in range(self.__graph.num_vertex):
                if i == j:
                    self.__matrix[i][j] = 0
                elif self.__graph.exist_edges(i, j):
                    self.__matrix[i][j] = self.__graph.weigth_edges(i, j)
                else:
                    self.__matrix[i][j] = np.inf
    
    @property
    def __reconstruct_camino_mas_corto(self):
        path = []
        if self.__distance[self.__start][self.__end] == -1:
            return None
        crawl = self.__start
        path.append(crawl+1)
        while crawl != self.__end:
            crawl = self.__distance[crawl][self.__end]
            path.append(crawl+1)
        self.__camino = path[::-1]
        return self.__camino
    
    @property
    def _paint_search_graph(self):
        camino = self.__camino
        if camino == None:
            newGraph = self.__graph.newGraph(0)   
            newGraph.paint_search_graph()
            return
        newGraph = self.__graph.newGraph(len(camino))   
        for i in range(0, len(camino)):
            newGraph.labelVertex(i, self.__graph.getLabel(camino[i]-1))
        for i in range(0, len(camino)):
            for j in range(0, len(camino)):
                if i != j:
                    newGraph.insert_edges_weigth(i, j, self.__graph.weigth_edges(camino[i]-1, camino[j]-1))
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        newGraph.print_graph_labeled
        newGraph.paint_search_graph()
        return newGraph
    
    @property
    def __printPath__(self):
        print("Algoritmo de Floyd Warshall")
        print(f"Camino más corto entre {self.__start + 1} y {self.__end + 1}:")
        print(f"Distancia: {self.__matrix[self.__start][self.__end]}")
        print("Camino:", self.__camino)
        print("Vertex \t\t Distance")
        for i in range(self.__graph.num_vertex):
            print(f"{i+1} \t\t {self.__matrix[i][self.__end]}")
        
    
    @property
    def floydWarshall(self):
        self.initMatrix
        for i in range(self.__graph.num_vertex):
            for j in range(self.__graph.num_vertex):
                if self.__matrix[i][j] != np.inf:
                    self.__distance[i][j] = j
                    self.__parent[i][j] = i
        
        for k in range(self.__graph.num_vertex):
            for i in range(self.__graph.num_vertex):
                for j in range(self.__graph.num_vertex):
                    if self.__matrix[i][j] > self.__matrix[i][k] + self.__matrix[k][j]:
                        self.__matrix[i][j] = self.__matrix[i][k] + self.__matrix[k][j]
                        self.__distance[i][j] = self.__distance[i][k]
                        self.__parent[i][j] = self.__parent[k][j]
        
        self.__reconstruct_camino_mas_corto
        self._paint_search_graph
        self.__printPath__
        return self.__matrix[self.__start][self.__end]