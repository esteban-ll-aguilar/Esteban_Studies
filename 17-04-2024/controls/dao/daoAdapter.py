from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List

T = TypeVar("T")

class DaoAdapter(Generic[T]):
    atype: Type[T]
    def __init__(self, atype: Type[T]):
        self.atype = atype
        self.lista = Linked_List()

        print(self.atype.__name__)

    def _list(self):
        return self.lista
    
    def _save(self, data: T) -> T:
        print(data.serialize)
        self.lista.add(data, self.lista._length)