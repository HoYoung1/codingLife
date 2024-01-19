from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.copy = nums
        self.nums = self.copy[:]

    def reset(self) -> List[int]:
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            return self.nums

# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)