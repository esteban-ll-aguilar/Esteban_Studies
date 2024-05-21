from controls.dao.daoAdapter import DaoAdapter
from models.censo import Censo
class CensoDao(DaoAdapter):
    def __init__(self):
        super().__init__(Censo)
        self.censo = None

    def get_censo(self):
        if self.censo == None:
            self.censo = Censo()
        return self.censo

    def set_censo(self, value):
        self.censo = value

    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self.get_censo()._id = self._lista._length + 1
        self._save(self.get_censo())


        