from models.persona import Persona
from controls.productoDaoControl import ProductoDaoControl
from controls.tda.linked.linkedList import Linked_List
from models.producto import Producto
class Factura:
    def __init__(self) -> None:
        self.__id = 0
        self.__fecha = ''
        self.__NComprobante = ''
        self.__personaId = None
        self.__iva = 0.0
        self.__total = 0.0
        self.__subtotal = 0.0
        self.__detalle = ''

    @property
    def _subtotal(self):
        return self.__subtotal

    @_subtotal.setter
    def _subtotal(self, value):
        self.__subtotal = value

    @property
    def _detalle(self):
        return self.__detalle

    @_detalle.setter
    def _detalle(self, value):
        self.__detalle = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _NComprobante(self):
        return self.__NComprobante

    @_NComprobante.setter
    def _NComprobante(self, value):
        self.__NComprobante = value

    @property
    def _personaId(self):
        if self.__personaId == None:
            self.__personaId = Persona()
        return self.__personaId

    @_personaId.setter
    def _personaId(self, value):
        self.__personaId = value

    @property
    def _iva(self):
        return self.__iva

    @_iva.setter
    def _iva(self, value):
        self.__iva = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

    @property
    def serialize(self):
        print('Factura Serialize:')
        return {
            'id': self._id,
            'fecha': self._fecha,
            'NComprobante': self._NComprobante,
            'personaId': self._personaId.serialize,
            'detalle': self._detalle,
            'subtotal': self._subtotal,
            'iva': self._iva,
            'total': self._total
        }
    def deserializar(self, data):

        factura = Factura()
        factura._id = data['id']
        factura._fecha = data['fecha']
        factura._NComprobante = data['NComprobante']
        factura._personaId = Persona().deserializar(data['personaId'])
        factura._detalle = data['detalle']
        factura._subtotal = data['subtotal']
        factura._iva = data['iva']
        factura._total = data['total']
        
        return factura
    
    
    def __str__(self) -> str:
        return f'Factura: {self.serialize}'