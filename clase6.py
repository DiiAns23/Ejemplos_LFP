class Lexico:
    contador = 0
    angular_abierta = 0
    igual = False

    def __init__(self):
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
        self.linea = 1
        self.columna = 0
    
    def Analizar(self, cadena):
        tkn = '' # Token
        while cadena != '':
            lexema = cadena[self.contador]
            tkn += self.Ignorar(lexema)
            print(tkn)

    def Ignorar(self, lexema):
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
            
            self.contador += 1
            return lexema


a = Lexico()
f = open('carpeta/entrada.txt', 'r')
input = f.read()
f.close()

analizar = a.Analizar(input)