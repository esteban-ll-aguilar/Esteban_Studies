
from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.persona import Persona

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Persona)
        self.__persona = None

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
            #self.__persona._id = self._list()._length
        return self.__persona
    
    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        #Falta ponerle el id
        self.__persona._id = self._lista._length +1
        print('Persona Dao Control:')
        print(self.__persona.serialize)
        self._save(self.__persona)

    def merge(self, pos):
        self._merge(self.__persona, pos)



""" #Alta ecuacion
from models.persona import Persona
from controls.tda.linked.linkedList import Linked_List
from controls.dao.daoAdapter import DaoAdapter
import json
class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        self.atype = Persona
        super().__init__(self.atype)
        self.__persona = None
        self.__lista = Linked_List()

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
            self.__persona._id = self.__lista._length
        return self.__persona
    
    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista
    
    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self.save(self.__persona)


    

       
        

    
 """