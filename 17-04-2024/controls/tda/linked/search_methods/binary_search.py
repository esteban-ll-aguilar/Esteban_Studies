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

    # def binary_search_models(self, data, attribute):
    #     while self.__izq <= self.__der:
    #         self.__mitad = (self.__izq + self.__der) // 2
    #         if getattr(self.__array[self.__mitad], attribute) == data:
    #             return self.__mitad, self.__array[self.__mitad]
    #         elif getattr(self.__array[self.__mitad], attribute) < data:
    #             self.__izq = self.__mitad + 1
    #         else:
    #             self.__der = self.__mitad - 1
    #     return Exception("Error")

    # def binary_search(self,array, data):
    #         first = 0
    #         last = len(array) - 1
    #         found = False

    #         while first <= last and not found:
    #             midpoint = (first + last) // 2
    #             if array[midpoint] == data:
    #                 found = True
    #             else:
    #                 if data < array[midpoint]:
    #                     last = midpoint - 1
    #                 else:
    #                     first = midpoint + 1
    #         return found, midpoint

        
        
        
        
            
            
        
                
                