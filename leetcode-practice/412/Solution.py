from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result: List[str] = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

assert Solution().fizzBuzz(3) == ["1","2","Fizz"]
assert Solution().fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
assert Solution().fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]



