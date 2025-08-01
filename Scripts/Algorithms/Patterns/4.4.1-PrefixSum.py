from collections import defaultdict

def sub_array_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] += 1
    return count



def calcPreFixSum(array):
    preFixSum = [0] * len(array)
    preFixSum[0] = array[0]

    for i in range(1, len(array)):
        preFixSum[i] = preFixSum[i - 1] + array[i]

    return preFixSum

arr = [1, 2, 3, 4, 5]
resultado = calcPreFixSum(arr)
print(resultado) 


"""
LeetCode 303

class NumArray:
    def __init__(self, nums: List[int]):
        # Construimos el arreglo de prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.prefix_sum = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left-1]

        

leetCode 560

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefix_sum_frequency = defaultdict(int)
        prefix_sum_frequency[0] = 1
        
        for num in nums:
            prefixSum += num

            if prefixSum - k in prefix_sum_frequency:
                count += prefix_sum_frequency[prefixSum - k]
            prefix_sum_frequency[prefixSum] += 1
        return count

"""