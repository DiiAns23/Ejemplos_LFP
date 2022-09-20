class Generador:

    generador = None

    def getInstance(self):
        if Generador.generador is None:
            Generador.generador = Generador()
        return Generador.generador
        
    def addExpresion(self, n1, n2, tipo):
        return f'({n1} {tipo} {n2})'

    def addTrigonometrica(self, n1, tipo):
        return f'{tipo}({n1})'
