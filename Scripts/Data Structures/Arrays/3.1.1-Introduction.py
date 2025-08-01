"""
#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
#In Python we only have dynamic arrays
#Some basic operations: 

#Look-up/Accses - O(1)
#Push/Pop - O(1)*
#Insert - O(n)
#Delete - O(n)
"""

array = [7, 12, 4, 19, 33, 21, 6, 15]

# Look up / Access O(1)
# Any element of an array can be accessed by it's index
firstElement = array[0]
sixthElement = array[5]

# Push / Pop O(1)
# Push corresponds to pushing or adding an element at the end of the array
# Since the index of the end is know, finding it and pushing or poping an element
# Adds 87 at the end of the array
array.append(57)

#In some special cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
#So when an element is to appended and the array is filled, the entire array has to be copied to a new location
#With more space allocated(generally double the space) this time so that more items can be appended.
#Therefore, some individual operations may reuire O(n) time or greater, but when averaged over a large number of operations,
array.pop() #Pops/removes the element at the end of the array in O(1) time.

print(array)

# Insert O(n)
# Inserts an element at the begining of the array, or at any location specified
#This is O(n) operation since after inserting the element at the desired location,
#The elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
#This requires looping through the array. Hence, O(n) time.
array.insert(0,50) #Inserts 50 at the beginning of the array and shifts all other elements one place towards right. O(n)
array.insert(4,0) #inserts '0' at index '4', thus shifting all elements starting from index 4 one place towards right. O(n)

print(array)


# Delete O(n)
#Similar to insert, it deletes an element from the specified location in O(n) time
#The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
#Hence, O(n) time complexity
# Pop delets the first element
array.pop(0)
print(array)

# This command removes the first ocurence of the element 17 in the array
array.remove(17)
print(array)

# This command deletes element fro position 2 to position 4
del array[2:4]
print(array)


