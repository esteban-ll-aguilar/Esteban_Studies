from typing import TypeVar, Generic, Type
from controls.tda.stack.stack import Stack
import os, json
T = TypeVar("T")

class StackDaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Stack(10)
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  + "/data/"
        #print('Url: '+self.URL)
        #print('Clase: '+self.atype.__name__)
    
    
    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            f.close()
            temp_list = []  # Lista temporal para almacenar los datos
            print("Datos: " + str(datos))
            for data in datos:
                temp_list.append(self.atype().deserializar(data))
            self.lista.clear
            # Insertar los elementos en orden inverso
            for item in reversed(temp_list):
                self.lista.push(item)
        return self.lista

    

    def __transform__(self):
        size = self.lista._stack._length
        aux = '['
        for i in range(size):
            aux += str(json.dumps(self.lista._stack.get(i).serialize)) 
            if i < size -1:
                aux += ','
        aux += ']'
        return aux
    
    
    
    @property
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._stack._length):
            aux.append(self.lista._stack.get(i)._id)
        return aux

    def _save(self, data: T) -> T:
        
        self._list()
        
        self.lista.push(data)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()

    def _merge(self, data: T, pos) -> T:
        self._list()
        self.lista._stack.edit(data, pos)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()