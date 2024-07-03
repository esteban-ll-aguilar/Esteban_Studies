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
from controls.tda.graph.graphLabeled import GraphLabeled
import time
    
pdc = PersonaDaoControl()
pdc._persona._nombre = "Esteban"
pdc._persona._apellidos = "Garcia"
pdc._persona._dni = "12345678A"
pdc._persona._telefono = "123456789"
pdc._persona._direccion = "Calle 123"
pdc._persona._tipoIdentificacion = "CEDULA"
pdc = pdc._persona.deserializar(pdc._persona.serialize)

pdc1 = PersonaDaoControl()
pdc1._persona._nombre = "Alicia"
pdc1._persona._apellidos = "Cabrera"
pdc1._persona._dni = "051654816s"
pdc1._persona._telefono = "123456789"
pdc1._persona._direccion = "Calle 123"
pdc1._persona._tipoIdentificacion = "CEDULA"
pdc1 = pdc1._persona.deserializar(pdc1._persona.serialize)

pdc2 = PersonaDaoControl()
pdc2._persona._nombre = "Juan"
pdc2._persona._apellidos = "Perez"
pdc2._persona._dni = "051654816s"
pdc2._persona._telefono = "123456789"
pdc2._persona._direccion = "Calle 123"
pdc2._persona._tipoIdentificacion = "CEDULA"
pdc2 = pdc2._persona.deserializar(pdc2._persona.serialize)



graph = GraphLabeled(5)
graph.insert_edges_weigth(0, 1, 10)
graph.insert_edges_weigth(0, 2, 20)
graph.insert_edges_weigth(1, 3, 20)
graph.setLabel(0, pdc)
graph.setLabel(1, pdc1)
graph.setLabel(2, pdc2)


graph.paint_graph_labeled
graph.print_graph_labeled