from Abstract.Instruccion import Instruccion

class Primitivos(Instruccion):
    def __init__(self,tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def getValor(self):
        return self.valor
        
    def interpretar(self, tree, table):
        return self.valor
        
    def getTipo(self):
        return self.tipo