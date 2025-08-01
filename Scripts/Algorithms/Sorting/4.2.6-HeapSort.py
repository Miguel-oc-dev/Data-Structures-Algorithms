"""
Heap Sort
Firts the array is converted into a binary heap, then the first element which is the maximun element in case of max heap
is swapped with the last element so that the maximum element goes to the end of the array
then the heap size is reduced by 1

Complexity: O(nlog N)
"""

count = 0

def maxHeap(array, heapSize, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    global count

    if left < heapSize:
        count += 1
        if array[left] > array[largest]:
            largest = left

    if right < heapSize:
        count += 1
        if array[right] > array[largest]:
            largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        maxHeap(array, heapSize, largest)

def buildHeap(array):
    heapSize = len(array)
    for i in range((heapSize // 2), -1,-1):
        maxHeap(array, heapSize, i)

def heapSort(array):
    heapSize = len(array)
    buildHeap(array)
    print(f'Heap: {array}')

    for i in range(heapSize - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapSize -= 1
        maxHeap(array, heapSize, 0)


array = [5,9,3,10,45,2,0]
heapSort(array)
print (array)
print(f'Number of comparisons = {count}')

sorted_array = [5,6,7,8,9]
heapSort(sorted_array)
print(sorted_array)
print(f'Number of comparisons = {count}')