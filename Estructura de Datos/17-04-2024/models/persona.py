from models.enumTipoTdentificacion import EnumTipoIdentificacion


class Persona:
    def __init__(self):
        self.__id = 0
        self.__apellidos = ''
        self.__nombre = ''
        self.__dni = ''
        self.__direccion = ''
        self.__telefono = ''
        self.__tipoIdentificacion = "EnumTipoIdentificacion.CEDULA"

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def serialize(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'apellidos': self._apellidos,
            'dni': self._dni,
            'direccion': self._direccion,
            'telefono': self._telefono,
            #'tipoIdentificacion': self.__tipoIdentificacion
            'tipoIdentificacion': self._tipoIdentificacion
        }

    def deserializar(self, data):
        persona = Persona()
        persona._id = data['id']
        persona._nombre = data['nombre']
        persona._apellidos = data['apellidos']
        persona._dni = data['dni']
        persona._direccion = data['direccion']
        persona._telefono = data['telefono']
        persona._tipoIdentificacion = data['tipoIdentificacion']
        return persona
        

    def __str__(self):
        return f'{self.__apellidos} {self.__nombre}'

    
