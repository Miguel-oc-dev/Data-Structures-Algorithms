"""
Data Structures
Lists

It's a structured data secuency, hetereogeneous and muteble
Diferent data types
"""

list = [29, True, 3.1415, "El numero PI es lo maximo"]

# We can see the data with it index, but if exceeds the limit throws an error
print(list[3])
print(list[-4])

# Sublist
print(list[1:3])

list[2] = "He cambiado este elemento"


new_list  = [1, 2, 3, 4, 5]

new_list.append(3)

print(new_list)
print(new_list.count(3))
print(new_list.index(4))
print(new_list.remove(3))


"""
Tuple

It's a structured data secuency, hetereogeneous and inmutable
"""

tuple = ("La tierra es plana", True, False)
print((1,))


"""
Set

It's a NO orderer, heteregenous, mutable without reply
"""

print(set([5, 2, 5, 1, 1.5]))
print(set([5, 2, 5, 1, 1.5]))
print(set("52511.5"))

# Uno de sus usos es eliminar los elementos repetidos de una secuencia
conjunto = set([2, 3, 3, 4])
print(conjunto)

# Agregar elemento
conjunto.add(1)
print(conjunto)

# Eliminar elemento
conjunto.remove(1)
print(conjunto)


# Operaciones de conjuntos
conjunto_2 = set([5, 3, 5, 6])
conjunto_3 = set([4, 2])

print(conjunto, conjunto_2, conjunto_3)
print(conjunto.intersection(conjunto_2))

# Issubset es para comprobar si los elementos de un conjunto estan dentro de otro
print(conjunto_2.issubset(conjunto))
print(conjunto_3.issubset(conjunto))

print(conjunto & conjunto_2)

"""
Operadores 
A | B - Union
A - B - Diferencia
A >= B - Superconjunto
A & B - Interseccion
A ^ B - Diferencia simetrica
A <= B - Subconjunto
"""

"""
Dictionaries

Relaciona elementos clave - valor

No tienen orden, son hetereogeneos y son mutables 
"""

# key - Values
diccionario = {1: "Uno", 2: "Dos"}
diccionario[3] = "Tres"
print(diccionario)

dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print(dict_lista_tuplas)

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

dict_tipos = {1: "Integer", 2.2: "Float", "texto": "String", (1, 2): "tupla"}
print(dict_tipos)

# Metodos, devuelven vistas dinamicas
print(diccionario, diccionario.key(), diccionario.values(), diccionario.items())

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
print(claves)
diccionario.pop(2)
print(diccionario)

