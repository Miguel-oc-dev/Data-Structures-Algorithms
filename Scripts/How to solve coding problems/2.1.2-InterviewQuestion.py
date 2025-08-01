"""
# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, 
# array1 = ['a','b','c','x'] , 
# array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.
"""

def xInBothArrays(array1, array2):

    letters = set(array1)
    for value in array2:
        if value in letters:
            return True
    
    return False

array1 = ['a', 'b', 'c', 'x']
array2 = ['x', 'y', 'z']
print(xInBothArrays(array1, array2))  # True

array1 = ['a', 'b', 'c']
array2 = ['x', 'y', 'z']
print(xInBothArrays(array1, array2))  # False


#One solution can be creating a dictionary for one of the arrays and then looping over the other array
#To check if any of its elements are present in the dictionary's keys.

def smarter_matching(array1, array2):
    dictionary = dict()

    for i in range(len(array1)):
        dictionary[array1[i]] = True

    for i in range(len(array2)):
        if array2[i] in dictionary:
            return True
        
    return False

print(smarter_matching(array1, array2))
