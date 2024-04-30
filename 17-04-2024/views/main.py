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
from controls.calculos import Calculos
from controls.tdaArray import TDAArray
from controls.tda.linked.linkedList import Linked_List
from controls.personaControl import PersonaControl
from controls.personaDaoControl import PersonaDaoControl
from controls.censoDao import CensoDao
import json
pc = PersonaControl()
cd = CensoDao()
pcd = PersonaDaoControl()
try:
    pc._persona._apellidos = "Leon"
    pc._persona._nombre = "Esteban"
    pc._persona._dni = "12345678"
    pc._persona._telefono = "0993114884"
    pc._persona._direccion = "Calle 1"
    pc.save
    pcd._persona._apellidos = "Leon"
    pcd._persona._nombre = "Esteban"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd._persona._apellidos = "Leon"
    pcd.save

    pc._persona = None
    pcd._persona = None
    pc._persona._nombre = "Christian"
    pc._persona._apellidos = "Robles"
    pc._persona._dni = "12345678"
    pc._persona._telefono = "0993114884"
    pc._persona._direccion = "Calle 1"
    pc.save
    pcd._persona._nombre = "Christian"
    pcd._persona._apellidos = "Robles"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd.save

    pc._persona = None
    pc._persona._nombre = "Santiago"
    pc._persona._apellidos = "Robles"
    pc._persona._dni = "12345678"
    pc._persona._telefono = "0993114884"
    pc._persona._direccion = "Calle 1"
    pc.save

    pc._persona = None
    pc._persona._nombre = "Jose"
    pc._persona._apellidos = "Guaman"
    pc._persona._dni = "12345678"
    pc._persona._telefono = "0993114884"
    pc._persona._direccion = "Calle 1"
    pc.save
    
    print("Lista de personas")
    print(pcd._lista)
    


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