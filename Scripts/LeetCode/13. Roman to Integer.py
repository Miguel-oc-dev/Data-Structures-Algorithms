"""


"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapa de valores romanos
        roman_dict= {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterar sobre los caracteres de la cadena de derecha a izquierda
        for char in reversed(s):
            current_value = roman_dict[char]
            
            # Si el valor actual es menor que el valor anterior, se resta
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Actualizar el valor previo
            prev_value = current_value

        return total