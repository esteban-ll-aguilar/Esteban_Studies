from controls.exception.arrayPositionException import ArrayPositionException
class ArrayList:
    def __init__(self):
        self.__array = []
        self.__length = 0


    @property
    def isEmpty(self):
        return self.__length == 0
    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    def __addLast__(self, data):
        self.__array.append(data)
        self.__length += 1
        
    def __addFirst__(self, data):
        self.__array.insert(0, data)
        self.__length += 1
    
    def add(self, data, pos):
        
        if self.__length == 0 and pos == 0:
            
            
            self.__addFirst__(data)
        elif pos == self.__length:
            self.__addLast__(data)
        else:
            self.__array.insert(pos, data)
            self.__length += 1
            
    def get(self, pos):
        if pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position is out of range")
        return self.__array[pos]
    
    def detele(self, pos):
        if pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Position is out of range")
        self.__array.pop(pos)
        for i in range(0, self.__length-1):
            print(self.__array[i])
            self.__array[i]._id = i+1
        self.__length -= 1
        
            
    @property
    def clear(self):
        self.__array.clear()
        self.__length = 0
        
    @property
    def print(self):
        print("Length: "+str(self.__length))
        print(self.__array)
            
    
        
        
        
    