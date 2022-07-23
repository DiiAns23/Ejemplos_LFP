print("Bienvenidos al curso de Lenguajes Formales y de Programacacion Seccion B+")
print("Esta es una clase de Bienvenida")

curso = "Lenguajes Formales y de Programacion"
edad = 21
nombre = "Diego Obin"

print("Ejemplo de un if")
if edad == 21:
    print(nombre)
    print(curso)

print("Ejemplo de un for")
for i in range(edad):
    print(i)

print("Ejemplo de un while")
while edad>0:
    print(edad)
    edad = edad-1

print("Recorriendo un array")
lista_numeros = [1,2,3.14159,4,5,6,7,'Este es un texto',9,"Este es un texto"]
for i in lista_numeros:
    print(i)