from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedListExeption import LinkedEmptyException
from controls.tda.array.arrayList import ArrayList

class StackOperation:
    def __init__(self, tope, useList):
        self.__class = Linked_List() if useList else ArrayList()
        self.__tope = tope

    @property
    def _class(self):
        return self.__class

    @_class.setter
    def _class(self, value):
        self.__class = value


    @property
    def verifyTop(self):
        return self.__class._length < self.__tope
    
    
    def push(self, data):
        if self.verifyTop:
            
            self._class.add(data,0)
            
        else:
            raise LinkedEmptyException("Stack is Full")
        
    @property
    def pop(self):
        if self.__class.isEmpty:
            raise LinkedEmptyException("List is Empty")
        else:
            self._class.detele(0)
            
    @property
    def _clear(self):
        self._class.clear

            
    


    
