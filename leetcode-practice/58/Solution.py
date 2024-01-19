class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

s = "Hello World"
assert Solution().lengthOfLastWord(s) == 5
s = "   fly me   to   the moon  "
assert Solution().lengthOfLastWord(s) == 4