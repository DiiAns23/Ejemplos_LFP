from TablaSimbolos.Tipo import TIPO
from TablaSimbolos.Excepcion import Excepcion

class Tabla_Simbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio es un Diccionario Vacio
        self.anterior = anterior #Al inicio no hay nada
    
    def getTablaG(self):
        return self.tabla

    def setTabla(self, simbolo):
        if simbolo.id in self.tabla:
            return Excepcion('Sintactico', 'Variable ya declarada', simbolo.getFila(), simbolo.getColum())
        else:
            self.tabla[simbolo.id] = simbolo
    
    def setTablaFuncion(self,simbolo):
        if simbolo.id in self.tabla:
            return "Asignacion"
        else:
            self.tabla[simbolo.id] = simbolo
    
    def getTabla(self, ide):
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            else:
                tablaActual = tablaActual.anterior
        return None
    
    def updateArray(self, simbolo, indices):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla:
                actual = tablaActual.tabla[simbolo.id].getValor()
                x = 0
                for indice in indices:
                    if x == (len(indices)-1):
                        try:
                            actual = actual[indice - 1]
                            actual.setValor(simbolo.getValor())
                            actual.setTipo(simbolo.getTipo())
                        except:
                            return Excepcion("Semantico","Indices fuera de rango", simbolo.getFila(), simbolo.getColum())
                    else:
                        try:
                            actual = actual[indice-1].getValor()
                        except:
                            return Excepcion("Semantico", "Indices fuera de rango", simbolo.getFila(), simbolo.getColum())
                    x += 1
                return None
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada", simbolo.getFila(), simbolo.getColum())
    
    def updateStruct(self, simbolo, claves):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla:
                actual = tablaActual.tabla[simbolo.id].getValor()
                x = 0
                for clave in claves:
                    if x == (len(claves)-1):
                        try:
                            actual = actual[str(clave)]
                            if actual.getTipo() == TIPO.NULO:
                                actual.setValor(simbolo.getValor())
                                actual.setTipo(simbolo.getTipo())
                            elif actual.getTipo() == simbolo.getTipo():
                                actual.setValor(simbolo.getValor())
                                actual.setTipo(simbolo.getTipo())
                            else:
                                return Excepcion("Semantico", "Los tipos no coinciden", simbolo.getFila(), simbolo.getColum())
                        except:
                            return Excepcion("Semantico", "No se han encontrado", simbolo.getFila(), simbolo.getColum())
                    else:
                        try:
                            actual = actual[str(clave)].getValor()
                        except:
                            return Excepcion("Semantico", "No se han encontrado los valores", simbolo.getFila(), simbolo.getColum())
                    x += 1
                return None
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada", simbolo.getFila(), simbolo.getColum())