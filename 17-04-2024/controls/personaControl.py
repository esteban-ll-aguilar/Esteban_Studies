#Alta ecuacion
from models.persona import Persona
from controls.tda.linked.linkedList import Linked_List
import json
class PersonaControl():
    def __init__(self):
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
        self.__lista.add(self.__persona, self.__lista._length)
        readjson = json.dumps(self._lista.toArray, indent=4)
        #guardar en archivo
        save_file = open("/home/esteban/Escritorio/Estudios Esteban/Ciclo 3/Estructura de datos/17-04-2024/persona.json", "w")
        save_file.write(readjson)
        save_file.close()
        #print(readjson)

       
        

    
