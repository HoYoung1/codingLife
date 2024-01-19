from typing import List



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        s = strs[0]
        if s == '':
            return ''

        idx = 0
        while idx < len(s):
            for str in strs:
                if len(str) == idx or str[idx] != s[idx]:
                    return s[:idx]
            idx += 1
        return s


strs = ["flower","flow","flight"]
assert Solution().longestCommonPrefix(strs) == 'fl'
strs = ["dog","racecar","car"]
assert Solution().longestCommonPrefix(strs) == ''
strs = ["a"]
assert Solution().longestCommonPrefix(strs) == 'a'
strs = ["flower","flower","flower","flower"]
assert Solution().longestCommonPrefix(strs) == 'flower'

