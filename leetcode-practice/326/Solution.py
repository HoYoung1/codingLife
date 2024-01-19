import math

# 틀림
# >>> math.log(243,3)
# >>> 4.999999999999999

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        c = math.log(n, 3)
        if c != int(c):
            return False
        return True

27
81
243

Solution().isPowerOfThree(27) == True
Solution().isPowerOfThree(0) == False
Solution().isPowerOfThree(-1) == False
