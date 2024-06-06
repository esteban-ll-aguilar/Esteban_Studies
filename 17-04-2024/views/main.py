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
from controls.personaControl import PersonaControl
from controls.personaDaoControl import PersonaDaoControl
from controls.censoDao import CensoDao
from controls.tda.stack.stack import Stack
from controls.tda.queque.queque import Queque
from controls.tda.linked.ordenation_methods.quickSort import QuickSort
from controls.tda.linked.ordenation_methods.selection import Selection
from controls.tda.linked.ordenation_methods.shell import Shell
from controls.tda.linked.search_methods.binary_search import BinarySearch

import time



lista = Linked_List()
pdc = PersonaDaoControl()
qs = QuickSort()
sl = Selection()
sll = Shell()

try:
    
    """ for i in range(10):
        list.append(i) """
        #lista.add(random.randint(-100, 100))  
    """ lista.print
    lista.sort(1)
    lista.print
    
    lista1 = Linked_List()
    lista1.add("Cale")
    lista1.add("Esteban")
    lista1.add("Alejandra")
    lista1.add("Cristian")
    lista1.add("Juan")

    lista1.print
    lista1.sort(0)
    lista1.print """

    
    
    """ pdc._list().print
    listaAux = pdc._list().sort_models("_apellidos", 1)
    listaAux.print """

    """ listita = lista1.search_number_equals('c')
    print("Listita")
    listita.print """
    list = []
    for i in range(4):
        list.append(random.randint(1, 10))
    
    print(list)
    #print(qs.quick_sort_acendent(list))
    #print(sl.selection_sort_descendent(list))
    #print(sll.shell_sort_desendent(list))
    list = qs.quick_sort(list)
    print(list)
    bs =BinarySearch(list)
    print(bs.binary_search(5))
    
    
    
    
except Exception as e:
    print(e)





















""" array = TDAArray(5)
array.save("Hola Cale")
array.save("Hola")
array.save("Hola 45698")

print(array.check()) """




""" c = Calculos()
c._mru._distancia = 45.0
c._mru._tiempo = 5.6
c.calcular_velocidad()
print(c._mru) """