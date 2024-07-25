#Alta ecuacion
from controls.dao.daoListAdapter import DaoListAdapter
from models.factura import Factura
import json, os
class FacturaListControl(DaoListAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None
        
    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
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
        
    def delete(self, pos):
        self._detele(pos)
        
    @property
    def _print(self):
        self.lista.print
        
    