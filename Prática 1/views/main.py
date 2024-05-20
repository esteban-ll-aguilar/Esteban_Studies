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
from controls.retencionListDaoControl import RetencionListDaoControl
from controls.personaListControl import PersonaListControl
from controls.facturaListControl    import FacturaListControl
from controls.tda.stack.stack import Stack
#import cProfile
import os
import psutil

pcd = PersonaListControl()
fdc = FacturaListControl()
rtldc = RetencionListDaoControl(useList=False, size=25)

""" pcd = PersonaDaoControl()
fdc = FacturaDaoControl()
rtldc = RetencionListDaoControl(useList=True, size=25)
pl = PersonaListControl() """
try:
    tiempo_programa = time()
    time_inicio = time()
    rtldc._retencion._clienteId = "0705743177111"
    rtldc._retencion._facturaId = "5454651151"
    rtldc._retencion._baseImponible = 4
    rtldc._retencion._fechaEmicion = "2024-05-19 01:55"
    rtldc._retencion._porcentajeRetencion = 0.08
    rtldc._retencion._totalRetenido = 0.32
    rtldc.save
    time_fin = time()
    print('-----------------------------------------------------------------------------------------')
    print('-------------------------            Listas Arrays         ---------------------------')
    print('-----------------------------------------------------------------------------------------')
    
    print("\nTiempo de ejecucion al guardar la retension: ", time_fin - time_inicio)
    print("\nMemoria usada en la lista De Persona: ", rtldc._lista._stack._class.__sizeList__,  "bytes")
    
    print('-----------------------------------------------------------------------------------------')
    time_inicio = time()
    pcd._persona._nombre = "Esteban"
    pcd._persona._apellidos = "Calle"
    pcd._persona._dni = "0705743177"   
    pcd._persona._direccion = "Calle 1"
    pcd._persona._correo = "@gamil.com"
    pcd._persona._telefono = "0987654321"
    pcd._persona._tipoIdentificacion = "Cedula"
    pcd.save
    time_fin = time()
    print('-----------------------------------------------------------------------------------------')
    
    print("\nTiempo de ejecucion al guardar la persona: ", time_fin - time_inicio)
    print("\nMemoria usada en la lista de Personas: ", pcd._lista.__sizeList__, "bytes")
    
    print('-----------------------------------------------------------------------------------------')
    
    time_inicio = time()
    fdc._factura._clienteId = "0705743177111"
    fdc._factura._fecha = "2024-05-19"
    fdc._factura._NComprobante = "5454651151"
    fdc._factura._iva = 0.12
    fdc._factura._total = 4.0
    fdc._factura._subtotal = 3.68
    fdc.save
    time_fin = time()
    tiempo_programa_fin = time()
    print('-----------------------------------------------------------------------------------------')
    
    print("\nTiempo de ejecucion al guardar la factura: ", time_fin - time_inicio)
    print("\nMemoria usada en la lista de Factura ", fdc._lista.__sizeList__, "bytes")
    
    print('-----------------------------------------------------------------------------------------')
    
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2
    print('-----------------------------------------------------------------------------------------')
    
    print("\nMemoria usada por el proceso: ", memory_usage, "MB")
    print("\nTiempo total de ejecucion del programa: ", tiempo_programa_fin - tiempo_programa)
    
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