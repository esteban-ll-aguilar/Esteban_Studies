from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os, json
T = TypeVar("T")

class DaoAdapter(Generic[T]):
    atype: Type[T]
    def __init__(self, atype: Type[T]):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  + "/data/"

        print(self.atype.__name__)
    
    
    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                a = self.atype.deserializar(data)
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
                
    
    def _save(self, data: T) -> T:
        self._list()
        self.lista.add(data, self.lista._length)
        f = open(self.URL + self.file, "w")
        f.write(self.__transform__())
        f.close()