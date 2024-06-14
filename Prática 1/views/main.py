#DAO
'''
Patron de diseno DAO PIS

Dao adapter
* create
* list
* update (change, stafe)
* search

'''

import sys
from time import time
sys.path.append('../')
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
from controls.personaListControl import PersonaListControl
from controls.facturaListControl    import FacturaListControl
from controls.tda.stack.stack import Stack
#import cProfile
import os
import psutil

pcd = PersonaDaoControl()
fdc = FacturaDaoControl()
rtldc = RetencionDaoControl()

""" pcd = PersonaDaoControl()
fdc = FacturaDaoControl()
rtldc = RetencionListDaoControl(useList=True, size=25)
pl = PersonaListControl() """
try:
    pcd._lista
    pcd._lista.sort_models("_nombre", 1, 1)
    print(pcd.to_dict_list())
    
except Exception as e:
    print(e)


#Listas Enlazadas
""" 
lista = Linked_List()
lista.__addLast__("Hola 1")
lista.__addLast__("Hola 2")
lista.__addLast__("Hola 3")
lista.__addLast__("Hola 4")
lista.__addLast__("Hola 5")


lista.__actualizeData__("Hola 6", 3)
print(lista._length)
lista.__str__()
print(lista)
 """




















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