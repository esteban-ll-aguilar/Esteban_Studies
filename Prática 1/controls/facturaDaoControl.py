from models.factura import Factura
from controls.dao.daoAdapter import DaoAdapter
class FacturaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None
    
    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
            #self.__factura._id = self._list()._length
        return self.__factura
    
    @_factura.setter
    def _factura(self, value):
        self.__factura = value
        
    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self.__factura._id = self._lista._length +1
        self._save(self.__factura)
        
        
    def merge(self, pos):
        self._merge(self.__factura, pos)
        