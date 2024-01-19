class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        result = ''
        while num:
            for k, v in symbol.items():
                if num >= v:
                    num -= v
                    result += k
                    break
        return result

# assert Solution().intToRoman(1994) == 'MCMXCIV'
# assert Solution().intToRoman(20) == 'XX'
# assert Solution().intToRoman(3) == 'III'
assert Solution().intToRoman(58) == 'LVIII'
