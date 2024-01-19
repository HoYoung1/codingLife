from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(set(prices))<2:
            return 0
        maxp = 0
        minp = prices[0]
        for i in range(1, len(prices)):
            maxp = max(maxp, prices[i] - minp)
            minp = min(minp, prices[i])
        return maxp