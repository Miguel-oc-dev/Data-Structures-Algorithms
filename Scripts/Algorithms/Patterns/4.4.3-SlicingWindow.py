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



def fixed_sliding_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum




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



def sliding_window(s):
    left = 0
    window = set()  # o dict, Counter dependiendo del problema
    max_len = 0

    for right in range(len(s)):
        # Expandir la ventana
        while s[right] in window:
            window.remove(s[left])
            left += 1

        window.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
