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
sys.path.append('../')
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.personaControl import PersonaControl
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
from controls.tda.stack.stack import Stack
pcd = PersonaDaoControl()
fcd = FacturaDaoControl()
rt = RetencionDaoControl()
st = Stack(5)
try:
    rt._retencion._fechaEmicion = "2021-07-10"
    rt._retencion._NRetencion = "001-001-000000001"
    rt._retencion.__baseImponible = "45.0"
    st.push(rt._retencion)
    st.push("Hola 2")
    
    #st.print
    
    
    rt._retencion._fechaEmicion = "2021-07-10"
    rt._retencion._NRetencion = "001 - 001 - 000000002"
    rt._retencion.__baseImponible = "45.0"
    rt.save    

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