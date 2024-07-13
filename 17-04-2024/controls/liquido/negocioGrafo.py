from controls.tda.graph.graphLabeledNoManaged import GraphLabeledManaged
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
            self.__grafo = GraphLabeledManaged(list._length)
            array = list.toArray
            for i in range(0, len(array)):
                self.__grafo.labelVertex(i, array[i])
            self.__grafo.print_graph_labeled
            self.__grafo.save_graph_labeled(file=self.__name)
        else:
            Exception("Lista vacia")                
    
    @property
    def get_graph(self):
        if self.__grafo is None:
            if self.fileExists:
                self.__grafo = GraphLabeledManaged(self.__ndao._lista._length)
                self.__grafo = self.__grafo.recontruct_graph(file=self.__name)
                self.__grafo.paint_graph_labeled
                return self.__grafo
            self.create_graph()
            return self.__grafo
        else:
            None
        
        
    
    @property
    def fileExists(self):
        url  = r'C:\Users\esteb\OneDrive\Escritorio\Estudios_Esteban\3-Ciclo\Estructura de Datos\Esteban_Studies\17-04-2024\data'
        url += '/'+self.__name
        #self.__grafo.fileExists(file=self.__name)
        return os.path.exists(url)
    @property
    def save_graph(self):
        self.__grafo.save_graph_labeled(file=self.__name)
    