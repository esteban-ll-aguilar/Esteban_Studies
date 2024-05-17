import enum

class EnumTipoIdentificacion(enum.Enum):
    RUCEDUCATIVO = 'RUC EDUCATIVO'
    RUCPROFESIONAL = 'RUC PROFESIONAL'
    

    def getValue(self):
        return self.value
    
    def __str__(self) -> str:
        return self.value
