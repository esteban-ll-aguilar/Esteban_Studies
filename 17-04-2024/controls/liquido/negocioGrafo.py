from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.liquido.negocioDaoControl import NegocioDaoControl
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
                self.__grafo.labelVertex(0, array[i])
            self.__grafo.paint_graph_labeled