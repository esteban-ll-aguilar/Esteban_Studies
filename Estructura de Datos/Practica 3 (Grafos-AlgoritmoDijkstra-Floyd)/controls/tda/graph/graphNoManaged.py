from controls.tda.graph.graphManaged import GraphManaged
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.graph.adjacent import Adjacent
from math import nan



class GraphNoManaged(GraphManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        
        
    def insert_edges_weigth(self, v1, v2, weigth):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.exist_edges(v1, v2):
                edg = self.num_edges + 1
                self.setNumEdges(edg)
                adj = Adjacent()
                adj._destination = v2
                adj._weigth = weigth
                
                adj1 = Adjacent()
                adj1._destination = v1
                adj1._weigth = weigth
                aux = self.adjacent(v1)
                aux1 = self.adjacent(v2)
                aux.add(adj, aux._length)
                aux1.add(adj1, aux1._length)
                
                
        else:
            raise ArrayPositionException("Delimites out")
    
    @property
    def allVertexConnected(self):
        return super().allVertexConnected
    
    def newGraph(self, num_vertex):
        return GraphNoManaged(num_vertex)
        
        
    
    