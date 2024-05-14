from controls.dao.daoAdapter import DaoAdapter
from models.producto import Producto
class ProductoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Producto)
        self.__producto = None
        
    @property
    def _producto(self):
        if self.__producto == None:
            self.__producto = Producto()
            #self.__producto._id = self._list()._length
        return self.__producto
    
    @_producto.setter
    def _producto(self, value):
        self.__producto = value
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__producto._id = self._lista._length +1
        print('Producto Dao Control:')
        self._save(self.__producto)
        
    def merge(self, pos):
        self._merge(self.__producto, pos)
        
        
        