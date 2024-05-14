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
from controls.productoDaoControl import ProductoDaoControl

pcd = PersonaDaoControl()
fcd = FacturaDaoControl()
prodcd = ProductoDaoControl()

try:
    
    
    
    """ pcd._persona._apellidos = "Leon"
    pcd._persona._nombre = "Esteban"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd._persona._apellidos = "Leon"
    pcd.save """
    
    """ producto1 = prodcd._producto    
    producto1._nombre = "Producto 1"
    producto1._precio = 10.0
    producto1._cantidad = 10
    prodcd.save """
    
    fcd._factura._personaId = pcd._list().get(0)
    fcd._factura._fecha = "2021-07-10"
    fcd._factura._NComprobante = "001-001-000000001"
    """ fcd._factura._producto._lista.add(producto1, fcd._factura._producto._lista._length)
    fcd._factura._producto._lista.add(producto1, fcd._factura._producto._lista._length) """
    fcd._factura._producto._producto._nombre = "Producto 1"
    fcd._factura._producto._producto._precio = 10.0
    fcd._factura._producto._producto._cantidad = 10
    fcd._factura._producto.save
    fcd._factura._producto._producto = None
    fcd._factura._producto._producto._nombre = "Producto 2"
    fcd._factura._producto._producto._precio = 10.0
    fcd._factura._producto._producto._cantidad = 10
    fcd._factura._producto.save
    
    fcd.save
    
    
    
    
    
    
    """ 

    pcd._persona._apellidos = "Leon"
    pcd._persona._nombre = "Esteban"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd._persona._apellidos = "Leon"
    pcd.save
    pcd._persona = None

    pcd._persona._nombre = "Christian"
    pcd._persona._apellidos = "Robles"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd.save

    
    pcd._persona = None

    pcd._persona._nombre = "Santiago"
    pcd._persona._apellidos = "Robles"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd.save

    pcd._persona = None

    pcd._persona._nombre = "Mishel"
    pcd._persona._apellidos = "Rodas"
    pcd._persona._dni = "12345678"
    pcd._persona._telefono = "0993114884"
    pcd._persona._direccion = "Calle 1"
    pcd._persona._tipoIdentificacion = "CEDULA"
    pcd.save """

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