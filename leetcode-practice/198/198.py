from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(dp)



assert Solution().rob([1,2,3,1]) == 4
assert Solution().rob([2,7,9,3,1]) == 12