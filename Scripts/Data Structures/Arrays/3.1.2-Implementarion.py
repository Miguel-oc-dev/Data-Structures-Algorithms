class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        # This method takes in the index of elment as a parameter and returns the corresponding element in O(1).
        return self.data[index]
    
    def push(self, item):
        self.length += 1
        # Adds the item provided to the end of the array
        self.data[self.length - 1] = item

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1] # Deletes the last element from array
        self.length -= 1
        return last_item
    
    def insert(self, index, item):
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1] # Shifts every element from the index to the end by one place
        self.data[index] = item

    def delete(self, index):
        for i in range(index, self.length - 1): # Shifts elements from the given index to the end by one place towards left
            self.data[i] = self.data[i + 1] # The last element which remains two times in the array is deleted
        del self.data[self.length - 1]
        self.length -= 1

arr = MyArray()
arr.push(6)
arr.push(2)
arr.push(9)

arr.pop()

arr.push(45)
arr.push(12)
arr.push(67)

arr.insert(3, 10)

arr.delete(4)

print(arr.get(1))
print(arr)