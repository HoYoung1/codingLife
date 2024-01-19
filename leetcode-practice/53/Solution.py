from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]

        result = dp[0] = nums[0]
        for i in range(1, len(nums)):
            # if dp[i-1]+nums[i] < nums[i]:
            #     dp[i] = nums[i]
            # else:
            #     dp[i] = dp[i-1] + nums[i]
            # 아래로 변경가능
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            result = max(dp[i], result)
        return result


# assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
# assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5,4,-1,7,8]) == 23

# -2 1 -3 4 -1 2 1 -5 4
# ---
# -2 1 -2 4 3 5 6 1 5 <-- dp 배열
#
# 5 4 -1 7 8 current or dp[current -1 ] + current
# ----
# 5 9 8 15 23
