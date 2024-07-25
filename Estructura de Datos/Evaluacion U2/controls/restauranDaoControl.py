from controls.dao.daoAdapter import DaoAdapter
from models.restaurant import Restaurant
class RestautanDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Restaurant)
        self.__restaurant = None
        
    @property
    def _restaurant(self):
        if self.__restaurant == None:
            self.__restaurant = Restaurant()
        return self.__restaurant
    
    @_restaurant.setter
    def _restaurant(self, value):
        self.__restaurant = value
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__restaurant._id = self._lista._length + 1
        self._save(self.__restaurant)
    
    def merge(self, pos):
        self._merge(self._restaurant, pos)
        
    