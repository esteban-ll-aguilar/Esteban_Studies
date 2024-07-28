#DAO
'''
Patron de diseno DAO PIS

Dao adapter
* create
* list
* update (change, stafe)
* search
Patron de diseno Fachada

'''

import sys
sys.path.append('../')
import random
from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.ordenation_methods.quickSort import QuickSort
from controls.tda.linked.ordenation_methods.selection import Selection
from controls.tda.linked.search_methods.binary_search import BinarySearch
from controls.tda.linked.search_methods.sequiential_binary_search import SequentialBinarySearch
from controls.tda.graph.graphManaged import GraphManaged
from controls.tda.graph.graphNoManaged import GraphNoManaged
from controls.tda.graph.graphLabeledManaged import GraphLabeledManaged
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.tda.graph.searchMethod.dijkstraAlgorithm import DijkstraAlgorithm
from controls.tda.graph.searchMethod.floydWarshallAlgorithm import FloydWarshallAlgorithm
from controls.modelGraphsControl.parqueGrafo import ParqueGrafo

from time import time

parque = ParqueGrafo()
graph = parque.get_graph
dijktra = DijkstraAlgorithm(graph,start=1, end=15)
dijktra.dijkstra
floy = FloydWarshallAlgorithm(graph, start=1,end=15)
floy.floydWarshall

print(graph.allVertexConnected)


inicio = time()
print("----------------- Algoritmo de Dijkstra -----------------")
dijktra = DijkstraAlgorithm(graph,start=1, end=15)
dijktra.dijkstra
tiempoDijkstra = time()-inicio

inicio = time()
print("----------------- Algoritmo de Floyd Warshall -----------------")
floy = FloydWarshallAlgorithm(graph, start=1,end=15)
floy.floydWarshall

print("Tiempo de ejecucion Dijkstra: ", tiempoDijkstra)
print("Tiempo de ejecucion Floyd Warshall: ", time()-inicio)
