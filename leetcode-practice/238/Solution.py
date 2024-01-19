from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]

        right = nums[-1]
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products

# 1 2 3 4
# 1 1 8 6


Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
Solution().productExceptSelf([[-1,1,0,-3,3]]) == [0,0,9,0,0]
