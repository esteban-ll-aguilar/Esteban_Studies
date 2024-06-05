from controls.tda.linked.node import Node
from controls.tdaArray import TDAArray
from controls.exception.linkedListExeption import LinkedEmptyException
from controls.exception.arrayPositionException import ArrayPositionException
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.insersion import Insersion
from numbers import Number

class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
            

    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element

    
    def delete(self, pos = 0):
        
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position out range")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == (self.__length - 1):
            return self.deleteLast()
        else:
            preview = self.getNode(pos - 1)
            actually = self.getNode(pos)
            element = preview._data
            next = actually._next
            actually = None
            preview._next = next
            self._length = self._length - 1
            return element

    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        try:
            return self.getNode(pos)._data
        except Exception as error:
            print(error)
            return None

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)
        
    @property
    def toArray(self):
        #array = TDAArray(self.__length)
        array = []
        
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self.__length:
                array.append(node._data)
                node = node._next
                cont += 1
        return array
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])
        
            
    def sort(self, type = 1):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], Number) or isinstance(array[0], str):
                #burbuja = Burbuja()
                insersion = Insersion()
                if type == 1:
                 #   array = burbuja.sort_burbuja_number_acendent(array)
                    array = insersion.sort_primitive_acendent(array)
                else:
                  #  array = burbuja.sort_burbuja_number_decendent(array)
                    array = insersion.sort_primitive_desendent(array)
            
            self.toList(array)
    
    def sort_models(self, attribute="_id",type = 1):
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                #burbuja = Burbuja()
                insersion = Insersion()
                if type == 1:
                 #   array = burbuja.sort_burbuja_objects_acendent(array, attribute)
                    array = insersion.sort_models_acendent(array, attribute)
                else:
                  #  array = burbuja.sort_burbuja_objects_decendent(array, attribute)
                    array = insersion.sort_models_descendent(array, attribute)
            self.toList(array)
        return self
    
        
    def search_number_equals(self, data):
        lista = Linked_List()
        if self.isEmpty:
            raise LinkedEmptyException("List empty")
        else:
            array = self.toArray
            for i in range(0, len(array)):
                if (array[i].lower().startswith(data.lower())):
                    lista.add(array[i], lista._length)

        return lista
            
    
            