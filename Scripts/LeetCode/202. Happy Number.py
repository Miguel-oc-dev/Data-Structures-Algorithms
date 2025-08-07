"""
Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Creamos un conjunto para registrar los números que ya hemos visto.
        number_seen = set()

        # Continuamos hasta que n sea 1 (caso feliz) o repitamos un número (ciclo)
        while n != 1:
            # Si ya vimos este número antes, hay un ciclo → no es feliz
            if n in number_seen:
                return False

            # Registramos el número actual en el conjunto
            number_seen.add(n)

            # Reemplazamos n por la suma de los cuadrados de sus dígitos
            # Convertimos n a string para iterar por cada dígito
            # Ejemplo: n = 19 → '1', '9' → 1^2 + 9^2 = 82
            n = sum(int(digit) ** 2 for digit in str(n))

        # Si salimos del bucle porque n == 1, entonces es un número feliz
        return True
