from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedListExeption import LinkedEmptyException
class StackOperation(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope
        



    @property
    def verifyTop(self):
        return self._length < self.__tope
    
    
    def push(self, data):
        if self.verifyTop:
            self.add(data,0)
        else:
            raise LinkedEmptyException("Stack is Full")
        
    @property
    def pop(self):
        if self.isEmpty:
            raise LinkedEmptyException("List is Empty")
        else:
            self.detele(0)
            
    @property
    def _clear(self):
        self.clear

            
    


    
