from typing import List
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        # 에라토스테네스의 체
        is_prime: List[bool] = [True for _ in range(n)] # initialize True
        if n <= 2:
            return 0
        is_prime[1] = is_prime[0] = False
        for i in range(2, int(math.sqrt(n-1)) + 1):
            if is_prime[i]:
                # i가 소수면, 모든 배수를 False함
                temp = i * 2
                while temp < n:
                    is_prime[temp] = False
                    temp += i
        return is_prime.count(True)

assert Solution().countPrimes(10) == 4
assert Solution().countPrimes(0) == 0
assert Solution().countPrimes(1) == 0