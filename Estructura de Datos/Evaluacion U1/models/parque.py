class Parque:
    def __init__(self):
        self.__id = 0 
        self.__nombre = ''
        self.__direccion = ''
        self.__detalle = ''
        self.__latitud = ''
        self.__longitud = ''


    @property
    def _longitud(self):
        return self.__longitud

    @_longitud.setter
    def _longitud(self, value):
        self.__longitud = value
        
    @property
    def _latitud(self):
        return self.__latitud

    @_latitud.setter
    def _latitud(self, value):
        self.__latitud = value

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
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value
        
    @property
    def _detalle(self):
        return self.__detalle

    @_detalle.setter
    def _detalle(self, value):
        self.__detalle = value

    @property
    def serialize(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'direccion': self._direccion,
            'latitud': self._latitud,
            'longitud': self._longitud,
            'detalle': self._detalle
        }
        
    def deserializar(self, data):
        parque = Parque()
        parque._id = data['id']
        parque._nombre = data['nombre']
        parque._direccion = data['direccion']
        parque._latitud = data['latitud']
        parque._longitud = data['longitud']
        parque._detalle = data['detalle']
        return parque
        
        
        
        