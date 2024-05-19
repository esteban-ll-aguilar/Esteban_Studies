from controls.tda.array.arrayList import ArrayList




class StackOperation(ArrayList):
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
            self.delete(0)
            
    @property
    def _clear(self):
        self.clear