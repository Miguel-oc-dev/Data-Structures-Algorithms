""" 
Dado un numero, tenemos que retornar su factorial
"""
def iterativeFactorial(number, f = 1):
    for i in range(1, number + 1):
        f = f * i
    return f

print(iterativeFactorial(0))
print(iterativeFactorial(5))
print(iterativeFactorial(50))


def recursiveFactorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursiveFactorial(number - 1)
    
print(recursiveFactorial(0))
print(recursiveFactorial(5))
print(recursiveFactorial(50))
print(recursiveFactorial(1000))