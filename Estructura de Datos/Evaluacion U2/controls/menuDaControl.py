from controls.dao.daoAdapter import DaoAdapter
from models.menu import Menu

class MenuDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Menu)
        self.__menu = None

    @property
    def _menu(self):
        if self.__menu == None:
            self.__menu = Menu()
        return self.__menu

    @_menu.setter
    def _menu(self, value):
        self.__menu = value


    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__menu._id = self._lista._length + 1
        self._save(self.__menu)
    
    def merge(self, pos):
        self._merge(self._menu, pos)