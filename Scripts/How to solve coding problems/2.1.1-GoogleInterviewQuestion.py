"""
This question is same as that in the Google interview question video.
We are given an array of integers and a particular sum.
We have to check if there are any two elements in the array that add up to the given sum.

For example, array = [1,2,4,5] ,sum = 6
This should return True as 2+4 = 6
"""

def hasPairWithSum(data, sum):
    
    # Se crea un set para almacenar los complementos
    unordered_sum = ()

    # Se itera por cada numero en la lista
    for value in data:
        # Si el valor actual ya esta en el conjunto, se encontro un par que suma el objetivo
        if value in unordered_sum:
            return True
        
        # Si no, se agrega el complemento para que sume con el valor actual y de el resultado
        unordered_sum.add(sum - value)
    return False