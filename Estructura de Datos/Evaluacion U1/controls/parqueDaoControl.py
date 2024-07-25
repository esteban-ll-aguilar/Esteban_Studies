from controls.dao.daoAdapter import DaoAdapter
from models.parque import Parque
class ParqueDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Parque)
        self.__parque = None

    @property
    def _parque(self):
        if self.__parque == None:
            self.__parque = Parque()
        return self.__parque

    @_parque.setter
    def _parque(self, value):
        self.__parque = value
        
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__parque._id = self._lista._length +1 
        self._save(self.__parque)
        
    def merge(self, pos):
        self._merge(self.__parque, pos)
        
    def delete(self, pos):
        self._delete(pos)
        

