from typing import TypeVar, Generic, Type
import os, json
from controls.tda.array.arrayList import ArrayList

T = TypeVar("T")
class DaoListAdapter:
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = ArrayList()
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
    
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._length):
            aux.append(self.lista._array[i].serialize)
        return aux
    
    def __transform__(self):
        aux = '['
        for i in range(0, self.lista._length):
            if i < self.lista._length -1:
                #print(self.lista.get(i).serialize)
                aux += str(json.dumps(self.lista.get(i).serialize)) + ','
            else:
                aux += str(json.dumps(self.lista.get(i).serialize))
        aux += ']'
        return aux
    
    def _save(self, data: T) -> T:
        self._list()
        self.lista.add(data, self.lista._length)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()
        
    def _detele(self, pos: int):
        self._list()
        self.lista.detele(pos)
        f = open(self.URL + self.file, "w")
        f.write(self.__transform__())
        f.close()
        
    