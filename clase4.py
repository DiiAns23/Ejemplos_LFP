from interfaz import * # importa todo el archivo interfaz
# import clase3 as C3# importa todo el archivo clase3
from clase3 import Analizador as Anali# importa la clase Analizador de clase3
from clase3 import Suma,Saludo

while True:
    a = PantPrin()
    if a.secundaria:
        PantSec()
    else:
        break

# alumnos = Anali.Lectura('carpeta/clase3.txt')
# if alumnos!= []:
#     a2 = Anali.Lectura('carpeta/clase3.txt')
#     for a in a2:
#         alumnos.append(a)

# for alumno in alumnos:
#     print(alumno.getNombre(),' ', alumno.getApellido(), ' ', alumno.getCorreo())


# print(Suma(2,4))
# print(Saludo('Damaris'))