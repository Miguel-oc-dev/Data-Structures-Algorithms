from collections import defaultdict

def use_hash_map(arr):
    hashmap = defaultdict(int)  # O usa dict() si no necesitas valores por defecto

    for i, val in enumerate(arr):
        # Ejemplo: contar frecuencia
        hashmap[val] += 1

        # Ejemplo: buscar complementos
        complement = target - val
        if complement in hashmap:
            return [hashmap[complement], i]

    return hashmap  # o el resultado buscado
