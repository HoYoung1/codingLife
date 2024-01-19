import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        eng = re.compile(r'[^a-zA-Z0-9]')
        eng_str = eng.sub('', s)
        eng_str = eng_str.lower()

        for i in range(len(eng_str)//2):
            if eng_str[i] != eng_str[len(eng_str)-1-i]:
                return False

        return True



s = "A man, a plan, a canal: Panama"
assert Solution().isPalindrome(s) == True
s = "race a car"
assert Solution().isPalindrome(s) is False
s = " "
assert Solution().isPalindrome(s) is True

