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
from controls.calculos import Calculos
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.personaDaoControl import PersonaDaoControl
from controls.censoDao import CensoDao
from controls.tda.stack.stack import Stack
from controls.tda.queque.queque import Queque
from controls.tda.linked.ordenation_methods.quickSort import QuickSort
from controls.tda.linked.ordenation_methods.selection import Selection
from controls.tda.linked.ordenation_methods.shell import Shell
from controls.tda.linked.search_methods.binary_search import BinarySearch
from controls.tda.linked.search_methods.sequiential_binary_search import SequentialBinarySearch
from controls.tda.graph.graphManaged import GraphManaged
from controls.tda.graph.graphNoManaged import GraphNoManaged
from controls.tda.graph.graphLabeledManaged import GraphLabeledManaged
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.liquido.negocioGrafo import NegocioGrafo
from controls.tda.tree.treeNumber import TreeNumber
from controls.tda.graph.searchMethod.dijkstraAlgorithm import DijkstraAlgorithm
from controls.tda.graph.searchMethod.floydWarshallAlgorithm import FloydWarshallAlgorithm
from controls.tda.tree.jug.node import Node as JugNode
from controls.tda.tree.jug.rules import Rules
from controls.tda.tree.jug.jugTree import JugTree

from time import time


# negocio = NegocioGrafo() 
# #negocio.create_graph()
# graph = negocio.get_graph
# graph.print_graph_labeled
# inicio = time()
# print("----------------- Algoritmo de Dijkstra -----------------")
# dijktra = DijkstraAlgorithm(graph,start=1, end=10)
# dijktra.dijkstra
# print("Tiempo de ejecucion Dijkstra: ", time()-inicio)
# inicio = time()
# print("----------------- Algoritmo de Floyd Warshall -----------------")
# floy = FloydWarshallAlgorithm(graph, start=1,end=10)
# floy.floydWarshall
# print("Tiempo de ejecucion Floyd Warshall: ", time()-inicio)






#En clase 
aux = "100,70,130,50,80,110,150,45,60,75,85,105,115,145,155"
nodeData =  aux.split(",")
tree = TreeNumber()
#247
for dat in nodeData:
    tree.insert(int(dat))

print(tree.getNroNodes)
print(tree.getLevels)
print(tree.getHeigth)
# print("-------------------------------------------------")
# print(tree.show_tree())
# tree.pre_orders().print
# tree.pos_orders().print
# tree.in_orders().print

node = JugNode()
nodeF = JugNode()

node.set_current_capacity(0,0)
nodeF.set_current_capacity(2,3)

justree = JugTree(node, nodeF)
result = justree.search()
if result is not None:
    print(justree.route(result))
    print("Lo logre: ", result)
else:
    print("No hay na'")