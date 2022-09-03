class Errores:
    def __init__(self, error, linea, columna):
        self.error = error
        self.linea = linea
        self.columna = columna
    
    def getError(self):
        return 'Error en la linea: ' + str(self.linea) + ' y columna: ' + str(self.columna) + ' Error:' + self.error