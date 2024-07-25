class Restaurant:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__codigoDePermiso = ''
        self.__estrellas = 0

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
    def _codigoDePermiso(self):
        return self.__codigoDePermiso

    @_codigoDePermiso.setter
    def _codigoDePermiso(self, value):
        self.__codigoDePermiso = value

    @property
    def _estrellas(self):
        return self.__estrellas

    @_estrellas.setter
    def _estrellas(self, value):
        self.__estrellas = value



    @property
    def serialize(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'codigoDePermiso': self._codigoDePermiso,
            'estrellas': self._estrellas,
        }
    
    def deserializar(self, data):
        self._id = data['id']
        self._nombre = data['nombre']
        self._codigoDePermiso = data['codigoDePermiso']
        self._estrellas = data['estrellas']
        return self