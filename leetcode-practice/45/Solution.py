import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize for _ in range(len(nums))]
        # dp[i] = i 번째 인덱스에 도달할 수 있는 가장 minimum 횟수
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

# 2 3 1 1 4
# 0 1 2 2 2



assert Solution().jump([2,3,1,1,4]) == 2
assert Solution().jump([2,3,0,1,4]) == 2

