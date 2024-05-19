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
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionListDaoControl import RetencionListDaoControl
from controls.personaListControl import PersonaListControl
from controls.tda.stack.stack import Stack
pcd = PersonaDaoControl()
fcd = FacturaDaoControl()
rt = RetencionListDaoControl()
p = PersonaListControl()
try:
    """ p._persona._nombre = "Esteban"
    p._persona._apellidos = "Calle"
    p._persona._dni = "12345678"
    p._persona._tipoIdentificacion = "DNI"
    p.save
    p.print """
    
    
    #{'id': 0, 'clienteId': '0705743177111', 'facturaId': '5454651151', 'fechaEmicion': '2024-05-19 01:55', 'baseImponible': '4', 'porcentajeRetencion': 0.08, 'totalRetenido': 0.32}
    
    rt = RetencionListDaoControl()
    rt._retencion._clienteId = "0705743177111"
    rt._retencion._facturaId = "5454651151"
    rt._retencion._baseImponible = 4
    rt._retencion._fechaEmicion = "2024-05-19 01:55"
    rt._retencion._porcentajeRetencion = 0.08
    rt._retencion._totalRetenido = 0.32
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