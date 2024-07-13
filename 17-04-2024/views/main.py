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
import time


negocio = NegocioGrafo()
#negocio.create_graph()
graph = negocio.get_graph
print(negocio.fileExists)

graph.insert_edges_weigth(0, 1, 2)
graph.insert_edges_weigth(0, 2, 5)

""" graph.insert_edges_weigth_E('1 El Dragon', '2 hola', 5)
graph.insert_edges_weigth_E('1 El Dragon', '3 El Esteban', 7)
graph.insert_edges_weigth_E('2 hola', '3 El Esteban', 9)
graph.insert_edges_weigth_E('2 hola', '1 El Dragon', 11) """

graph.print_graph_labeled
graph.paint_graph_labeled
negocio.save_graph

""" aux = "100,7,130,50,80,110,150,45,60,75,85,105,115,145,155,23"
nodeData =  aux.split(",")
tree = TreeNumber()

for dat in nodeData:
    tree.insert(int(dat))

print(tree.getNroNodes)
print(tree.getLevels)
print(tree.getHeigth) """