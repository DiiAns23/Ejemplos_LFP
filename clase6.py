from Errores import *
class Lexico:
    contador = 0
    angular_abierta = 0
    igual = False

    def __init__(self, cadena):
        self.errores = []
        self.tokens_reservadas = {
            'Tipo'      : 't_TIPO',
            'Operacion' : 't_OPERACION',
            'Numero'    : 't_NUMERO',
            '<'         : 't_AA',
            '>'         : 't_AC',
            '='         : 't_IGUAL',
            '/'         : 't_DIV',
        }

        self.tokens_operaciones = {
            'SUMA'    : 't_SUMA',
            'RESTA'   : 't_RESTA',
            'MULTITPLICACION'    : 't_MULT',
            'DIVISION'    : 't_DIV',
        }
        self.errores = ['?']
        self.cadena = cadena
        self.linea = 1
        self.columna = 1
    
    def Analizar(self):
        tkn = '' # Token
        getToken = ''
        while self.cadena != '':
            lexema = self.cadena[self.contador]
            tkn += self.Ignorar(lexema)
            if lexema != '>':
                getToken = self.getToken(tkn)
            if getToken == 't_TIPO' and self.angular_abierta ==2:
                self.cadena = self.cadena[self.contador:]
                self.angular_abierta = 0
                self.contador = 0

    def Tipo(self):
        tkn = '' # Token
        getToken = ''
        while self.cadena != '':
            lexema = self.cadena[self.contador]
            tkn += self.Ignorar(lexema)
            if lexema != '>':
                getToken = self.getToken(tkn)
            if getToken == 't_OPERACION' and self.igual == True:
                self.cadena = self.cadena[self.contador:]
                self.igual = False
                self.contador = 0
                return self.getOperacion()

    def getOperacion(self):
        ''

    def getToken(self, cadena):
        tkn = cadena
        if tkn in self.tokens_reservadas:
            return self.tokens_reservadas[tkn]
        elif tkn in self.tokens_operaciones:
            return self.tokens_operaciones[tkn]
        return ''
    def Ignorar(self, lexema):
        if lexema not in self.errores:
            if lexema == ' ':
                self.columna += 1
                self.contador += 1
                return ''
            elif lexema == '\n':
                self.columna = 0
                self.linea += 1
                self.contador += 1
                return ''
            elif lexema == '\t':
                self.columna += 4
                self.contador += 1
                return ''
            else:
                if lexema == '<' or lexema == '>':
                    self.angular_abierta += 1 # Si esta en 1, es una angular abierta, si esta en 2, es una angular cerrada
                    self.contador += 1
                    return ''
                elif lexema == '=':
                    self.igual = True
                    self.contador += 1
                    return ''
                self.columna += 1
                self.contador += 1
                return lexema
        else:
            self.contador += 1
            error = Errores(lexema, self.linea, self.columna)
            self.errores.append(error)
            return ''

    def getErrores(self):
        return self.errores

f = open('carpeta/entrada.txt', 'r')
input = f.read()
f.close()
a = Lexico(input)
a.Analizar()