import time

array = ['a','b','c','d','e']

def logAllPairs(array):
    # Esta función tiene bucles for anidados, pero solo hay un array de variables. Por lo tanto, no necesitamos dos variables para la función Big-O.
    for i in range(len(array)): # n * O(n)
        for j in range(len(array)): # n * O(n)
            print(array[i], array[j]) # n * O(1)

logAllPairs(array)

"""
Complejidad temporal total de la función logAllPairs =
    O(n*n + n*n + n*n*1) = O(3n^2)
Las constantes se pueden ignorar sin problemas.
Por lo tanto, O(3n^2) = O(n^2)
"""

newArray = [1,2,3,4,5]

def printNumbersThenPairs(array):
    # There are a total of three loops here, but only one variable
    print("The numbers are: ") #O(1)
    for i in range(len(array)): #O(n)
        print(array[i]) #n*O(1)

    print("The pairs are: ") #O(1)
    for i in range(len(array)): #n*O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i], array[j]) #n*n*O(1)

printNumbersThenPairs(newArray)