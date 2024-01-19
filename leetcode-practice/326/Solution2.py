import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False

            # n 이 3으로 나누어 떨어지면
            n = n // 3
        return True



# 27
# 81
# 243

Solution().isPowerOfThree(27) == True
Solution().isPowerOfThree(0) == False
Solution().isPowerOfThree(-1) == False
