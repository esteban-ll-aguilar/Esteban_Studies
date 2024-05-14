from controls.exception.arrayPositionException import ArrayPositionException

class TDAArray():
    def __init__(self, size, value= None):
        self.__size = size
        self.__position = 0
        if size > 0: 
            self.__array = []
            for i in range(0, self.__size):
                self.__array.append(None)
            print(self.__array)
        else: 
            self.__array = None

    @property
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value


    #def save(self, value):
     #   for i in range(0, self.__size):
      #      if self.__array[i] == None:
       #         self.__array[i] = value
        #        self.__espacios_disponibles = self.__size - i-1
         #       return 
        #raise ArrayPositionException('Index found error: La tabla esta llena')
    
    def save(self, value):
        #if self.__array[0] == None:
            self._array[self.__position] = value
            self.__position +=1
            print(self.__array)
       #else:
           # self._array[self.__position] = value
            #self.__position = self.__position + 1
    
    def check(self):
        #print("Espacios disponibles: ", self.__espacios_disponibles)
        #print(self._array)
        i = 0
        for j in range(0, self._size):
            if self.__array[j] == None:
                i = j
                break
        return i
    

    # proyectar cuantos se van a queda, quien tiene el mejor rendimirnto por cada materia, 