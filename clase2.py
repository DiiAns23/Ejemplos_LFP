# Ejemplo de clase 2

# LEER INFORMACION DE UN ARCHIVO
# Abrir el archivo
objeto = open('carpeta/clase2.ext','r+')

# Imprimir informacion dentro del archivo

# Lee todo el contenido del archivo
print("READ")
print(objeto.read())
# Cerramos el archivo
objeto.close()

objeto = open('carpeta/clase2.ext','r+')
# Lee un caracter de una linea
print("READLINE")
print(objeto.readline(1))
# Cerramos el archivo
objeto.close()

objeto = open('carpeta/clase2.ext','r+')
# Lee todas lineas, linea por linea
print("READLINES")
print(objeto.readlines())
# Cerramos el archivo
objeto.close()


# ESCRIBIR EN UN ARCHIVO
objeto = open('carpeta/clase2.ext','a')
objeto.write('\n\tEste texto fue agregado desde Python :3')
# Cerramos el archivo
objeto.close()

# LISTAS Y DICCIONARIOS

# LISTAS

lista1 = [1,2,3,4,5,6,7,8]
print(lista1) # [1,2,3,4,5,6,7,8]

lista1.append(9)
lista1.append(10)
print(lista1) # [1,2,3,4,5,6,7,8,9,10]


# DICCIONARIO
diccionario1 = {1:'Gato', 2:'Perro', 3: 'Caballo', 4:lista1}
print(diccionario1)

print(diccionario1[3])
print(diccionario1[4][6])

print("AGREGANDO UN DICCIONARIO A UNA LISTA")
lista2 = [
    {1:'Nombre', 2:'Apellido', 3:'Curso'}, # 0
    {1:'Nombre', 2:'Apellido', 3:'Curso'}, # 1
    {1:'Nombre', 2:'Apellido', 3:'Curso'} #2
    ] 

print(lista2[1][2])

