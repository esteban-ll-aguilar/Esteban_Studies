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
pcd1._persona._id = 1
pcd1._persona._nombre = "Esteban"
pcd1._persona._apellidos = "Cruz"
pcd1._persona._telefono = "0999999999"
pcd1._persona._dni = "0999999999"
pcd1._persona._direccion = "Loja"
pcd1._persona._tipoIdentificacion = "CEDULA"
pcd1._persona.deserializar(pcd1._persona.serialize)
pcd1 = pcd1._persona
pcd2 = PersonaDaoControl()
pcd2._persona._id = 2
pcd2._persona._nombre = "Juan"
pcd2._persona._apellidos = "Perez"
pcd2._persona._telefono = "0999999999"
pcd2._persona._dni = "0999999999"
pcd2._persona._direccion = "Loja"
pcd2._persona._tipoIdentificacion = "CEDULA"
pcd2._persona.deserializar(pcd2._persona.serialize)
pcd2 = pcd2._persona
pcd3 = PersonaDaoControl()
pcd3._persona._id = 3
pcd3._persona._nombre = "Pedro"
pcd3._persona._apellidos = "Perez"
pcd3._persona._telefono = "0999999999"
pcd3._persona._dni = "0999999999"
pcd3._persona._direccion = "Loja"
pcd3._persona._tipoIdentificacion = "CEDULA"
pcd3._persona.deserializar(pcd3._persona.serialize)
pcd3 = pcd3._persona



graph = GraphManaged(3)
graph.insert_edges_weigth_models(pcd1, pcd2, 10)
graph.insert_edges_weigth_models(pcd2, pcd1, 20)
graph.insert_edges_weigth_models(pcd2, pcd3, 30)
graph.insert_edges_weigth_models(pcd3, pcd2, 40)


graph.print_model
graph.paint_graph_model
