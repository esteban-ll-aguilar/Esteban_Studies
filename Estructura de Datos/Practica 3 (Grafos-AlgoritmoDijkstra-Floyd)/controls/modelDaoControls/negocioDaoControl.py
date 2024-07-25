from controls.dao.daoAdapter import DaoAdapter
from models.negocio import Negocio
class NegocioDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Negocio)
        self.__negocio = None

    @property
    def _negocio(self):
        if self.__negocio == None:
            self.__negocio = Negocio()
        return self.__negocio

    @_negocio.setter
    def _negocio(self, value):
        self.__negocio = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__negocio._id = self._lista._length + 1
        self._save(self.__negocio)
    
        
    