class Jug():
    def __init__(self) -> None:
        self.__capacity = 0
        self.__current_capacity = 0

    @property
    def _capacity(self):
        return self.__capacity

    @_capacity.setter
    def _capacity(self, value):
        self.__capacity = value

    @property
    def _current_capacity(self):
        return self.__current_capacity

    @_current_capacity.setter
    def _current_capacity(self, value):
        self.__current_capacity = value

    def __str__(self) -> str:
        return f"J{self.__capacity}L=>{self.__current_capacity} L" 
        