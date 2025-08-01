class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Primer filtro, si s y t no tienen la misma longitud, no pueden ser anagramas
        if len(s) != len(t):
            return False

        # Se crean diccionarios para contar la recuencia de cada letra en cada palabra
        first_word = {}
        second_word = {}

        # Se recorre el indice de s y t simultaneamente
        for start_index in range(len(s)):
            # Se actualiza el contador de letras en first_word para la cadena s
            first_word[s[start_index]] = 1 + first_word.get(s[start_index], 0)
            # Se actualiza el contador de letras en second_word para la cadena t
            second_word[t[start_index]] = 1 + second_word.get(t[start_index], 0)
            # dict.get(clave, 0) significa: "devuélveme el valor de esta clave si existe, si no, devuélveme 0".

        # Se comparan ambos diccionarios
        return first_word == second_word