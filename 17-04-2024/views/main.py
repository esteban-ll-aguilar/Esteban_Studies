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
import time

graph = GraphLabeledNoManaged(5)

pdc = PersonaDaoControl()
pdc._persona._nombre = "Esteban"
pdc._persona._apellidos = "Garcia"
graph.labelVertex(0, pdc._persona)


pdc._persona = None
pdc._persona._nombre = "Esteban"
pdc._persona._apellidos = "Garcia"
graph.labelVertex(0, pdc._persona)


print(graph.getVertex(pdc._persona))