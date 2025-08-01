"""

1. Fixed Sliding Window
    Sirve para encontrar subarrays o substrings de una determinada longitud
2. Dynamic Sliding Windw
    Sirve para encontrar el subarray o substring mas corto o que satisfaga una condicion
"""

# Fixed Slicing Window
# Dado un arreglo de enteros, encuentra la maxima suma de una subcadena de longitud k

def fixed_window(nums, k):
    # Inicializamos la suma maxima y la suma actual con la suma de los primeros k elementos
    max_sum = current_sum = sum(nums[:k])

    # Recorremos la lista desde el inidice k hasta el final
    for i in range(k, len(nums)):
        # Movemos la ventana sumando el nuevo elemento (nums[i])
        current_sum += nums[i] - nums[i - k]
        # Actualizamos la suma maxima si la suma actual es mayor
        max_sum = max(max_sum, current_sum)

    # Retornamos la suma maxima encontrada en cualquier ventana
    return max_sum

nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(fixed_window(nums, k))



# Dynamic Sliding Window
# Se usa cuando la longitud de la ventana depende de alguna condicion, como una sua o caracteres unicos

def dynamic_window(s):
    # Conjunto para rastrear los caracteres unicos en la ventana
    char_set = set()
    # Puntero inicial
    left = 0
    # Longitud maxima encontrada
    max_length = 0

    # Recorremos con el puntero derecho
    for right in range(len(s)):
        # Si el caracter actual ya esta en el conjunto, se reduce la ventana
        while s[right] in char_set:
            # Elimina el caracter duplicado
            char_set.remove(s[left])
            left += 1

        # Agregamos el caracter actual a la ventana
        char_set.add(s[right])

        # Calculamos la longitud de la ventana actual y actualizamos la maxima
        max_length = max(max_length, right - left + 1)
    return max_length

s = "abcabcbb"
print(dynamic_window(s))