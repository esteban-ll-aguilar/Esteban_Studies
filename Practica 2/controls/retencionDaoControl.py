from models.retencion import Retencion
from controls.dao.daoAdapter import DaoAdapter

class RetencionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Retencion)
        self.__retencion = None


    @property
    def _retencion(self):
        if self.__retencion == None:
            self.__retencion = Retencion()
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value
        
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__retencion._id = self._lista._length +1
        self._save(self.__retencion)
        
        
    
    

    