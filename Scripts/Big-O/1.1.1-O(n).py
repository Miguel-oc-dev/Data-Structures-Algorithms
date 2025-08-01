import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo' for i in range(100000)]

def findNemo(array):
    t0 = time.time()
    for i in range(0, len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f"Call to find Nemo took: {t1-t0} seconds.")

findNemo(nemo)
findNemo(everyone)
findNemo(large)


# Excersise 1
def funChallenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        stranger = True # n * O(1)
        a += 1 # n * O(1)

    return a # O(1)

"""
Tiempo total de ejecución de la función funchallenge =
O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n + 3) = O(3(n + 1))

    Cualquier constante en la notación Big-O puede ser reemplazada por 1, ya que no importa realmente qué constante sea.

    Por lo tanto, O(3(n + 1)) se convierte en O(n + 1)

    De manera similar, cualquier número constante sumado, restado, multiplicado o dividido por n puede escribirse simplemente como n.

    Esto se debe a que la constante que opera sobre n no depende de n, es decir, del tamaño de la entrada.

    Por lo tanto, se puede decir que la función funchallenge tiene una complejidad de O(n), o complejidad temporal lineal.
"""

# Ejercicio 2
def anotherFunChallenge(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)
    for i in range(input): # O(n)
        x = i + 1 # n * O(1)
        y = i + 2 # n * O(1)
        z = i + 3 # n * O(1)

    for j in range(input): # O(n)
        p = j * 2 # n * O(1)
        q = j * 2 # n * O(1)

    who_am_i = "I don't know" # O(1)