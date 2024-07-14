from controls.tda.graph.graphLabeledNoManaged import GraphLabeledManaged
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.liquido.negocioDaoControl import NegocioDaoControl
import os, sys
class NegocioGrafo:
    def __init__(self):
        print(sys.path[0])
        self.__name = os.path.basename((__file__)).replace('.py', '.json')
        self.__grafo = None
        self.__ndao = NegocioDaoControl()
        
    def create_graph(self):
        list = self.__ndao._lista
        if list._length > 0:
            self.__grafo = GraphLabeledNoManaged(list._length)
            array = list.toArray
            for i in range(0, len(array)):
                self.__grafo.labelVertex(i, array[i])
            self.__grafo.print_graph_labeled
        else:
            Exception("Lista vacia")                
    
    @property
    def get_graph(self):
        self.create_graph()
        if self.__grafo.fileExists(self.__name):
            self.__grafo = self.__grafo.recontruct_graph_labeled_with_lat_long(file=self.__name,atype=self.__grafo, model=NegocioDaoControl)
        self.__grafo.save_graph_labeled(file=self.__name)
        self.__grafo.paint_graph_labeled
        return self.__grafo
    
    
        
    @property
    def save_graph(self):
        self.__grafo.save_graph_labeled(file=self.__name)
        
    @property
    def obtainWeigths(self):
        return self.__grafo.obtain_weigths(graph=self.__grafo, file=self.__name)
    