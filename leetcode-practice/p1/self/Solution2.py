from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = [[idx, num] for idx, num, in enumerate(nums)]
        nums_with_idx.sort(key=lambda x: x[1])

        start, end = 0, len(nums) - 1
        while start <= end:

            s = nums_with_idx[start][1] + nums_with_idx[end][1]
            if s == target:
                return [nums_with_idx[start][0],  nums_with_idx[end][0]]
            elif s > target:
                end -= 1
            else:
                start += 1


assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
assert Solution().twoSum([3,2,4], 6) == [1,2]

