from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os, json
T = TypeVar("T")

class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  + "/data/"

    
    
    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                a = self.atype().deserializar(data)
                self.lista.add(a, self.lista._length)
            f.close()
        return self.lista
    
    
    def __transform__(self):
        aux = '['
        for i in range(0, self.lista._length):
            if i < self.lista._length -1:
                aux += str(json.dumps(self.lista.get(i).serialize)) + ','
            else:
                aux += str(json.dumps(self.lista.get(i).serialize))
        aux += ']'
        return aux
                
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista.get(i).serialize)
        return aux
    
    def to_dict_lista(self):
        aux = []
        for i in range(0, self.lista._length):
            aux.append(self.lista.get(i).serialize)
        return aux

            
    def _get(self, id):
        list = self._list()
        array = list.toArray
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None


    def _save(self, data: T) -> T:
        print("Guardando")
        self._list()
        self.lista.add(data, self.lista._length)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()

    def _merge(self, data: T, pos) -> T:
        print("Guardando")
        self._list()
        self.lista.edit(data, pos)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()