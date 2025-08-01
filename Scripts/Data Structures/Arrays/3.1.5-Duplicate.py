"""
#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false
"""

def duplicated(array):
    seen = set() # Conjunto vacio para guardar los elementos vistos

    # Recorre cada elemento del arreglo
    for item in array:
        # Si el elemento ya esta en el conjunto
        if item in seen:
            return True
        # Si no esta, entonces se agrega al conjunto
        seen.add(item)
    return False

array = [1,2,46,32,98,61,34,46]
print(duplicated(array))