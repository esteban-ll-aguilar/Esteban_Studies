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
import time



lista = Linked_List()
pdc = PersonaDaoControl()
try:
    
    for i in range(10):
        lista.add(random.randint(-100, 100))  
    lista.print
    lista.sort(1)
    lista.print
    
    lista1 = Linked_List()
    lista1.add("Hola")
    lista1.add("Mundo")
    lista1.add("Cruel")
    lista1.print
    lista1.sort(0)
    lista1.print
    
    pdc._list().print
    listaa = pdc._list().sort_models("_apellidos", 1)
    listaa.print
    
    
    
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