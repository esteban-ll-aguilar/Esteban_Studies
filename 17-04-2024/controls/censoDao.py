from controls.dao.daoAdapter import DaoAdapter
from models.censo import Censo
class CensoDao(DaoAdapter):
    def __init__(self):
        super().__init__(Censo)
        