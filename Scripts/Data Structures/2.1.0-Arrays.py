"""
Arrays (Lists)

En Python la estructura mas parecida a un array clasico es la list
    Ordenada
    Permite elementos repetidos
    Permite diferentes tipos de datos, aunque normalmente se usan homogéneos
"""

numbers = [10, 20, 30, 40]


"""
Operación	                Ejemplo	                    Complejidad
Acceso por índice	        numeros[2]	                O(1)
Modificar valor	            numeros[1] = 25	            O(1)
Insertar al final	        numeros.append(50)	        O(1) amortizado
Insertar en posición	    numeros.insert(1, 15)	    O(n)
Eliminar por valor	        numeros.remove(20)	        O(n)
Eliminar por índice	        numeros.pop(2)	            O(n)
Longitud	                len(numeros)	            O(1)
Iterar	                    for n in numeros: print(n)	O(n)
Ordenar	                    numeros.sort()	            O(n log n)

"""

# Operaciones utiles
a = [1, 2, 3, 4]
b = [4, 5, 6]

# Concatenar
c = a + b
print(c)

# Repetir
d = a * 2
print(d)

# Sublistas (slicing)
print(c[1:4])

# Contar ocurrencias
print(c.count(2))

# Indice de primer elemento
print(c.index(3))


"""
Casos de uso comunes

Representar secuencias (listas de usuarios, números, etc.)
Acumular resultados en bucles
Resolver problemas de sumas, búsqueda de máximos/mínimos
Simular estructuras como pilas o colas
"""

def groceries():
    groceries = ["apple", "banana", "carrots", "olive oil", "avocados"]

    # Cantidad del array
    print(f"Number of groceries: {len(groceries)}")

    # Imprime todo el arreglo
    for item in groceries:
        print(item, end = ", ")
    print()

    # Recupera el elemento constantemente
    print("Grocery item at index 3: ", groceries[3])

    # Elimina el elemento
    groceries[3] = None;

    # Checar longitud
    print("Number of groceries: ", len(groceries))

    for item in groceries:
        print(item, end = ", ")
    print()


if __name__ == "__main__":
    groceries()