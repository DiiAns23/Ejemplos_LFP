from expression import *
from operador import Operador

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, column):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, column)
    
    def ejecutar(self):
        izq = self.left.ejecutar()
        der = self.right.ejecutar()
        if self.tipo == Operador.SUMA:
            return izq + der
        elif self.tipo == Operador.RESTA:
            return izq - der
        elif self.tipo == Operador.MULTIPLICACION:
            return izq * der
        elif self.tipo == Operador.DIVISION:
            if der != 0:
                return izq / der
            else:
                print("Error: Division por cero")
                return None
        elif self.tipo == Operador.POTENCIA:
            return izq ** der
        elif self.tipo == Operador.MODULO:
            return izq % der
        else:
            return 0
