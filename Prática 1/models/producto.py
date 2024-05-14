class Producto:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__cantidad = 0
        self.__precio = 0.0

    @property
    def _cantidad(self):
        return self.__cantidad

    @_cantidad.setter
    def _cantidad(self, value):
        self.__cantidad = value

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
    def serialize(self):
        return {
            'idProduct': self._id,
            'nombre': self._nombre,
            'precio': self._precio,
            'cantidad': self._cantidad,
        }
    def deserializar(self, data):
        producto = Producto()
        producto._id = data['idProduct']
        producto._nombre = data['nombre']
        producto._precio = data['precio']
        producto._cantidad = data['cantidad']
        return producto
    
    def __str__(self):
        return f'Producto: {self._nombre}'
    