class Retencion:
    def __init__(self) -> None:
        self.__id = 0
        self.__NRetencion = ''
        self.__fechaEmicion = ''
        self.__facturaId = ''
        self.__clienteId = ''
        self.__baseImponible = 0.0
        self.__porcentajeRetencion = 0.0
        self.__totalRetenido = 0.0
        
        
    @property
    def _NRetencion(self):
        return self.__NRetencion

    @_NRetencion.setter
    def _NRetencion(self, value):
        self.__NRetencion = value

    @property
    def _clienteId(self):
        return self.__clienteId
    
    @_clienteId.setter
    def _clienteId(self, value):
        self.__clienteId = value
        

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fechaEmicion(self):
        return self.__fechaEmicion

    @_fechaEmicion.setter
    def _fechaEmicion(self, value):
        self.__fechaEmicion = value

    @property
    def _facturaId(self):
        return self.__facturaId

    @_facturaId.setter
    def _facturaId(self, value):
        self.__facturaId = value

    @property
    def _baseImponible(self):
        return self.__baseImponible

    @_baseImponible.setter
    def _baseImponible(self, value):
        self.__baseImponible = value

    @property
    def _porcentajeRetencion(self):
        return self.__porcentajeRetencion

    @_porcentajeRetencion.setter
    def _porcentajeRetencion(self, value):
        self.__porcentajeRetencion = value

    @property
    def _totalRetenido(self):
        return self.__totalRetenido

    @_totalRetenido.setter
    def _totalRetenido(self, value):
        self.__totalRetenido = value



    @property
    def serialize(self):
        return {
            'id': self._id,
            'clienteId': self._clienteId,
            'facturaId': self._facturaId,
            'fechaEmicion': self._fechaEmicion,
            'baseImponible': self._baseImponible,
            'porcentajeRetencion': self._porcentajeRetencion,
            'totalRetenido': self._totalRetenido
        }

    def deserializar(self, data):
        retencion = Retencion()
        retencion._id = data['id']
        retencion._clienteId = data['clienteId']
        retencion._facturaId = data['facturaId']
        retencion._fechaEmicion = data['fechaEmicion']
        retencion._porcentajeRetencion = data['porcentajeRetencion']
        retencion._baseImponible = data['baseImponible']
        retencion._totalRetenido = data['totalRetenido']
        
        return retencion