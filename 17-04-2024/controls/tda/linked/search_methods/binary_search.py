class BinarySearch:
    def __init__(self, array):
        self.__der = len(array) - 1
        self.__izq = 0
        self.__mitad = 0
        self.__array = array
    
    def binary_search(self, data):
        while self.__izq <= self.__der:
            self.__mitad = (self.__izq + self.__der) // 2
            if self.__array[self.__mitad] == data:
                return self.__mitad, self.__array[self.__mitad]
            elif self.__array[self.__mitad] < data:
                self.__izq = self.__mitad + 1
            else:
                self.__der = self.__mitad - 1
        return Exception("Error")
    
    """ def binary_search(self, data):
        if self.__izq < self.__der:
            return Exception("Error")
        elif len(self.__array) == 1:
            return self.__array
        
        self.__mitad = (self.__izq + self.__der) // 2
        
        
        if self.__array[self.__mitad] == data:
            return self.__mitad
        
        elif self.__array[self.__mitad] < data:
            self.__izq = self.__mitad + 1
            return self.binary_search(data)
        else:
            self.__der = self.__mitad - 1
            return self.binary_search(data) """

        
        
        
        
        
            
            
        
                
                