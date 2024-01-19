class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

s = "the sky is blue"
assert Solution().reverseWords(s) == "blue is sky the"
s = "  hello world  "
assert Solution().reverseWords(s) == "world hello"
s = "a good   example"
assert Solution().reverseWords(s) == "example good a"

