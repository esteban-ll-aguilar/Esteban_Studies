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
import time

pcd1 = PersonaDaoControl()
pcd1._persona._id = 0
pcd1._persona._nombre = "Esteban"
pcd1._persona._apellidos = "Cruz"
pcd1._persona._telefono = "0999999999"
pcd1._persona._dni = "0999999999"
pcd1._persona._direccion = "Loja"
pcd1._persona._tipoIdentificacion = "CEDULA"
pcd1._persona.deserializar(pcd1._persona.serialize)
pcd1 = pcd1
pcd2 = PersonaDaoControl()
pcd2._persona._id = 1
pcd2._persona._nombre = "Juan"
pcd2._persona._apellidos = "Perez"
pcd2._persona._telefono = "0999999999"
pcd2._persona._dni = "0999999999"
pcd2._persona._direccion = "Loja"
pcd2._persona._tipoIdentificacion = "CEDULA"
pcd2._persona.deserializar(pcd2._persona.serialize)


graph = GraphManaged(2)




graph.print
graph.paint_graph_model
