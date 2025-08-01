"""
Given a number, we have to return the number at that index of the Fibonacci sequence
0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .

The pattern of sequence is that each value is the sum of the 2 previous values,
that means that for N=5
"""

def fibonacci(number):
    # Caso base: si el numero es 0 o 1, solamente se regresa el valor
    if number <= 1:
        return number
    # Inicializamos los dos primeros terminos de la serie
    a, b = 0, 1
    print(f"F(0) = {a}")
    print(f"F(1) = {b}")
    for i in range(2, number + 1):
        a, b = b, a + b
        print(f"F({i}) = {b}")
    return b

fibonacci(7)


def fibonacciRecursive(number):
    if number < 2:
        return number
    return fibonacciRecursive(number-1) + fibonacciRecursive(number-2)
fibonacciRecursive(7)