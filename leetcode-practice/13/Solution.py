# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# IV = 4
# IX = 9
# XL = 40
# XC = 90
# CD = 400
# CM = 900
from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        dic: Dict[str, int] = {'CM': 900,
         'CD': 400,
         'XC': 90,
         'XL': 40,
         'IX': 9,
         'IV': 4,
         'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1}

        result = 0

        j = 0
        while j<len(s):
            for text, numeral in dic.items():
                if s[j:j+len(text)] == text:
                    result += numeral
                    j += len(text)
                    break
        return result


assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("MCMXCIV") == 1994