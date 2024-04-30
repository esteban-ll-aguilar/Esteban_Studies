from models.persona import Persona
class Censo:
    def __init__(self):
        self.__id = 0
        self.__fecha = ''
        self.__nene = Persona()
        self.__peso = 0.0
        self.__estatura = ''   

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _nene(self):
        return self.__nene

    @_nene.setter
    def _nene(self, value):
        self.__nene = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

    @property
    def _estatura(self):
        return self.__estatura

    @_estatura.setter
    def _estatura(self, value):
        self.__estatura = value
     