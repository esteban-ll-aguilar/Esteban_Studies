class Menu:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__precio = 0
        self.__restauranteId = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _restauranteId(self):
        return self.__restauranteId

    @_restauranteId.setter
    def _restauranteId(self, value):
        self.__restauranteId = value
        
    @property
    def serialize(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'precio': self._precio,
            'restauranteId': self._restauranteId,
        }
        
    def deserializar(self, data):
        self._id = data['id']
        self._nombre = data['nombre']
        self._precio = data['precio']
        self._restauranteId = data['restauranteId']
        return self

        
    
        
        
        
        
        