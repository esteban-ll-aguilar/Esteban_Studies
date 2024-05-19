#Alta ecuacion
from controls.dao.daoListAdapter import DaoListAdapter
from models.persona import Persona
import json, os
class PersonaListControl(DaoListAdapter):
    def __init__(self):
        super().__init__(Persona)
        self.__persona = None
        
    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona
    
    @_persona.setter
    def _persona(self, value):
        self.__persona = value
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__persona._id = self._lista._length +1
        self._save(self.__persona)
        
    @property
    def _print(self):
        self.lista.print
        
    