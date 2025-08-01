"""
Dado un arreglo con n números únicos en el rango 0 a n, encuentra el número que falta.

Entrada:
Un arreglo arr con n elementos únicos, donde cada uno está entre 0 y n (inclusive), excepto uno que falta.

Salida esperada:
El número que falta.

Ejemplo 1:
Entrada: arr = [3, 0, 1]
Salida esperada: 2
"""

def valorReal(array):
    n = len(array)

    sumaEsperada = n * (n+1) // 2
    sumaReal = sum(array)
    valor = sumaEsperada-sumaReal
    return valor

array = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(valorReal(array))
