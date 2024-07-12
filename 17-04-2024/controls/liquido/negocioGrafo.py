from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.liquido.negocioDaoControl import NegocioDaoControl
import sys
class NegocioGrafo:
    def __init__(self) -> None:
        self.__grafo = None
        self.__ndao = NegocioDaoControl()
        
    def create_graph(self):
        list = self.__ndao._lista
        if list._length > 0:
            self.__grafo = GraphLabeledNoManaged(list._length)
            array = list.toArray
            for i in range(0, len(array)):
                self.__grafo.labelVertex(i, array[i])
                
    @property
    def get_graph(self):
        if self.__grafo is None:
            Exception("Grafo no creado")
        return self.__grafo
    
    @property
    def save_graph(self):
        name = sys.path[0]
        print(name)
        #self.__grafo.save_graph_labeled()
    
    