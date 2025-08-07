"""
Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max_length: longitud máxima de una ventana válida
        # largest_count: cuenta del carácter más frecuente en la ventana actual
        max_length, largest_count = 0, 0

        # arr: contador de caracteres en la ventana actual
        arr = collections.Counter()

        for index in range(len(s)):
            # Añadimos el carácter actual al contador
            arr[s[index]] += 1

            # Actualizamos el carácter más frecuente visto en la ventana
            largest_count = max(largest_count, arr[s[index]])

            # Si la ventana actual necesita más de k reemplazos para igualar todos los caracteres
            # es decir, si el número de caracteres distintos al más frecuente es mayor que k
            if max_length - largest_count >= k:
                # Disminuimos el contador del carácter que está fuera de la nueva ventana
                arr[s[index - max_length]] -= 1
            else:
                # Si no necesitamos más de k reemplazos, expandimos la ventana
                max_length += 1

        # max_length es la longitud de la ventana más larga encontrada
        return max_length
