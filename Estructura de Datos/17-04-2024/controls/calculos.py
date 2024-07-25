from models.mru import Mru
class Calculos:
    def __init__(self):
        self.__mru =  Mru()

    @property
    def _mru(self):
        return self.__mru

    @_mru.setter
    def _mru(self, value):
        self.__mru = value

    #TODO 
    # x = v*t
    def calcular_velocidad(self):
        self._mru._velocidad = self.__mru._distancia / self.__mru._tiempo

        return self._mru._velocidad