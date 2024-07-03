from math import nan 
class Adjacent:
    def __init__(self):
        self.__weigth = nan
        self.__destination = nan

    @property
    def _weigth(self):
        return self.__weigth

    @_weigth.setter
    def _weigth(self, value):
        self.__weigth = value

    @property
    def _destination(self):
        return self.__destination

    @_destination.setter
    def _destination(self, value):
        self.__destination = value
        
        
    

        